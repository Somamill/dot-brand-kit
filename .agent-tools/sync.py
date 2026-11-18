"""Check/update documentation-only agent requirements from the approved public repo."""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import tempfile
import urllib.request

REPOSITORY = 'Somamill/dot-brand-kit'
FILES = ('AGENT_DEVELOPMENT.md', 'TOOL_CATALOG.md', 'LOCALIZATION.md',
         'APP_STORE_PLAYBOOK.md', 'TREND_RESEARCH.md', 'LANGUAGES.json')
LIMIT = 500_000


def download(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'dot-agent-policy'}), timeout=25) as response:
        data = response.read(LIMIT + 1)
    if len(data) > LIMIT:
        raise ValueError('Policy resource exceeds size limit')
    return data


def fetch(revision=None):
    if revision is None:
        revision = json.loads(download('https://api.github.com/repos/' + REPOSITORY + '/git/ref/heads/main'))['object']['sha']
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('Revision must be a full commit SHA')
    base = 'https://raw.githubusercontent.com/' + REPOSITORY + '/' + revision + '/'
    manifest = json.loads(download(base + 'agent-policy/manifest.json'))
    if manifest.get('schemaVersion') != 1 or set(manifest.get('files', {})) != set(FILES):
        raise ValueError('Unexpected policy manifest')
    payload = {}
    for name in FILES:
        entry = manifest['files'][name]
        if entry.get('path') != 'docs/' + name or not re.fullmatch(r'[0-9a-f]{64}', entry.get('sha256', '')):
            raise ValueError('Unexpected policy path or hash')
        data = download(base + entry['path'])
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError('Policy hash mismatch: ' + name)
        data.decode('utf-8')
        if name.endswith('.json'):
            json.loads(data)
        payload[name] = data
    return revision, manifest, payload


def validate_target(root):
    tools = root / '.agent-tools'
    target = tools / 'requirements'
    if tools.is_symlink() or target.is_symlink():
        raise ValueError('Managed policy directories must not be symlinks')
    if target.exists():
        for path in target.iterdir():
            if path.is_symlink() or not path.is_file() or path.name not in {*FILES, 'source.json'}:
                raise ValueError('Unexpected local policy content; preserved for inspection')
    return target


def current(target, manifest, payload):
    source = target / 'source.json'
    if not source.is_file():
        return False
    info = json.loads(source.read_text())
    if info.get('repository') != REPOSITORY or not re.fullmatch(r'[0-9a-f]{40}', info.get('commit', '')):
        raise ValueError('Invalid local policy provenance')
    if info.get('files') != {name: manifest['files'][name]['sha256'] for name in FILES}:
        return False
    return all((target / name).is_file() and (target / name).read_bytes() == data for name, data in payload.items())


def apply(root, revision, manifest, payload):
    target = validate_target(root)
    if current(target, manifest, payload):
        return False
    if target.exists():
        dirty = subprocess.check_output(['git', '-C', str(root), 'status', '--porcelain',
            '--untracked-files=all', '--ignored', '--', '.agent-tools/requirements'], text=True)
        if dirty:
            raise ValueError('Local policy changes preserved; commit or inspect them before updating')
    parent = target.parent
    parent.mkdir(exist_ok=True)
    lock = parent / '.requirements-sync-lock'
    lock.mkdir()  # A concurrent sync must not replace the same directory.
    stage = None
    backup = parent / '.requirements-previous'
    try:
        if backup.exists() or backup.is_symlink():
            raise ValueError('Previous policy backup preserved; inspect it before retrying')
        stage = pathlib.Path(tempfile.mkdtemp(prefix='.requirements-stage-', dir=parent))
        for name, data in payload.items():
            (stage / name).write_bytes(data)
        info = {'schemaVersion': 1, 'repository': REPOSITORY, 'commit': revision,
                'policyVersion': manifest['policyVersion'],
                'files': {name: manifest['files'][name]['sha256'] for name in FILES}}
        (stage / 'source.json').write_text(json.dumps(info, indent=2) + '\n')
        if target.exists():
            target.rename(backup)
        try:
            stage.rename(target)
        except OSError:
            if backup.exists():
                backup.rename(target)
            raise
        if backup.exists():
            shutil.rmtree(backup)
        return True
    finally:
        if stage is not None and stage.exists():
            shutil.rmtree(stage)
        lock.rmdir()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--update', action='store_true', help='Update managed documentation; never source code/design files')
    parser.add_argument('--revision', help='Optional full reviewed commit instead of current approved main')
    args = parser.parse_args()
    root = pathlib.Path(__file__).resolve().parents[1]
    try:
        revision, manifest, payload = fetch(args.revision)
        target = validate_target(root)
        if args.update:
            changed = apply(root, revision, manifest, payload)
            print('Policy updated; review and commit managed documentation.' if changed else 'Policy content is current.')
            return 0
        if current(target, manifest, payload):
            print('Policy content matches approved revision ' + revision)
            return 0
        print('Policy is missing or stale. Run with --update; review the resulting diff.')
        return 1
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print('Policy sync stopped; existing files preserved: ' + str(error))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
