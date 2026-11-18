"""Policy updates must preserve local work and reject untrusted resource paths."""
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import tempfile
import unittest
from unittest import mock
import urllib.error

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('policy_sync', ROOT / '.agent-tools/sync.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


def fixture(text=b'policy'):
    payload = {name: (b'{}' if name.endswith('.json') else text) for name in sync.FILES}
    manifest = {'schemaVersion': 1, 'policyVersion': 2, 'files': {
        name: {'path': 'docs/' + name, 'sha256': hashlib.sha256(data).hexdigest()}
        for name, data in payload.items()}}
    return manifest, payload


class PolicyTests(unittest.TestCase):
    def commit(self, root):
        for args in [('init', '-q'), ('add', '.'), ('commit', '-qm', 'fixture')]:
            subprocess.run(['git', '-C', str(root), '-c', 'core.hooksPath=/dev/null',
                '-c', 'user.name=Policy test', '-c', 'user.email=policy@example.invalid', *args],
                check=True, capture_output=True)

    def test_downloads_are_commit_pinned_and_hash_checked(self):
        manifest, payload = fixture()
        urls = []
        def download(url):
            urls.append(url)
            return json.dumps(manifest).encode() if url.endswith('manifest.json') else payload[url.rsplit('/', 1)[1]]
        with mock.patch.object(sync, 'download', side_effect=download):
            revision, _, result = sync.fetch('a' * 40)
        self.assertEqual(result, payload)
        self.assertTrue(all('/' + revision + '/' in url for url in urls))
        manifest['files']['TOOL_CATALOG.md']['path'] = '../escape.py'
        with mock.patch.object(sync, 'download', side_effect=download), self.assertRaises(ValueError):
            sync.fetch('a' * 40)
        with mock.patch.object(sync, 'download') as network, self.assertRaises(ValueError):
            sync.fetch('../main')
        network.assert_not_called()

    def test_bad_hash_is_rejected(self):
        manifest, payload = fixture()
        def download(url):
            return json.dumps(manifest).encode() if url.endswith('manifest.json') else b'tampered'
        with mock.patch.object(sync, 'download', side_effect=download), self.assertRaises(ValueError):
            sync.fetch('a' * 40)

    def test_update_preserves_design_and_does_not_churn_identical_content(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            (root / 'DESIGN.md').write_text('project-owned')
            (root / 'AGENTS.md').write_text('owner rules')
            manifest, payload = fixture()
            self.assertTrue(sync.apply(root, 'a' * 40, manifest, payload))
            target = root / '.agent-tools/requirements'
            self.assertTrue(sync.current(target, manifest, payload))
            self.assertFalse(sync.apply(root, 'b' * 40, manifest, payload))
            self.assertEqual(json.loads((target / 'source.json').read_text())['commit'], 'a' * 40)
            self.assertEqual((root / 'DESIGN.md').read_text(), 'project-owned')
            self.assertEqual((root / 'AGENTS.md').read_text(), 'owner rules')

    def test_dirty_or_unexpected_local_work_is_not_overwritten(self):
        for case in ['dirty', 'untracked']:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as temporary:
                root = pathlib.Path(temporary)
                manifest, payload = fixture()
                sync.apply(root, 'a' * 40, manifest, payload)
                self.commit(root)
                target = root / '.agent-tools/requirements'
                path = target / ('TOOL_CATALOG.md' if case == 'dirty' else 'notes.md')
                path.write_text('local work')
                manifest, payload = fixture(b'new policy')
                with self.assertRaises(ValueError):
                    sync.apply(root, 'b' * 40, manifest, payload)
                self.assertEqual(path.read_text(), 'local work')

    def test_clean_committed_bundle_updates(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            manifest, payload = fixture()
            sync.apply(root, 'a' * 40, manifest, payload)
            self.commit(root)
            manifest, payload = fixture(b'new policy')
            self.assertTrue(sync.apply(root, 'b' * 40, manifest, payload))
            self.assertTrue(sync.current(root / '.agent-tools/requirements', manifest, payload))

    def test_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            (root / '.agent-tools').mkdir()
            (root / 'external').mkdir()
            (root / '.agent-tools/requirements').symlink_to(root / 'external', target_is_directory=True)
            manifest, payload = fixture()
            with self.assertRaises(ValueError):
                sync.apply(root, 'a' * 40, manifest, payload)
            self.assertFalse(list((root / 'external').iterdir()))

    def test_failed_install_restores_previous_bundle(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            manifest, payload = fixture()
            sync.apply(root, 'a' * 40, manifest, payload)
            self.commit(root)
            manifest, payload = fixture(b'new policy')
            rename = pathlib.Path.rename
            def fail_stage(path, target):
                if path.name.startswith('.requirements-stage-'):
                    raise OSError('simulated rename failure')
                return rename(path, target)
            with mock.patch.object(pathlib.Path, 'rename', fail_stage), self.assertRaises(OSError):
                sync.apply(root, 'b' * 40, manifest, payload)
            target = root / '.agent-tools/requirements'
            self.assertEqual((target / 'TOOL_CATALOG.md').read_bytes(), b'policy')
            self.assertFalse((target.parent / '.requirements-sync-lock').exists())
            self.assertFalse((target.parent / '.requirements-previous').exists())

    def test_offline_check_reports_failure_without_changing_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            with mock.patch.object(sync, '__file__', str(root / '.agent-tools/sync.py')), \
                 mock.patch('sys.argv', ['sync.py']), \
                 mock.patch.object(sync, 'fetch', side_effect=urllib.error.URLError('offline')):
                self.assertEqual(sync.main(), 2)
            self.assertFalse((root / '.agent-tools').exists())

    def test_manifest_matches_sources_and_future_language_baseline(self):
        manifest = json.loads((ROOT / 'agent-policy/manifest.json').read_text())
        self.assertEqual(set(manifest['files']), set(sync.FILES))
        for entry in manifest['files'].values():
            self.assertEqual(hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest(), entry['sha256'])
        languages = json.loads((ROOT / 'docs/LANGUAGES.json').read_text())
        self.assertGreaterEqual(len({x['uiTag'] for x in languages['languages']}), 10)
        self.assertEqual(languages['default'], 'system-preferred-supported-language')
        self.assertEqual(languages['implementationStatus'], 'future-requirement-not-implemented-by-policy')


if __name__ == '__main__':
    unittest.main()
