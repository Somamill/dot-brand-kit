#if os(macOS)
import AppKit
import SwiftUI

private struct ControlSpecimen: View {
    let dark: Bool
    @State private var enabled = true
    @State private var disabledSetting = false
    @State private var playing = false

    var body: some View {
        VStack(alignment: .leading, spacing: DotMetrics.spaceLg) {
            VStack(alignment: .leading, spacing: DotMetrics.spaceXs) {
                Text("dot. controls").font(.largeTitle.weight(.semibold))
                Text(dark ? "Dark appearance" : "Light appearance")
                    .foregroundStyle(.secondary)
            }
            Divider()
            Text("Actions").font(.headline)
            HStack(spacing: DotMetrics.spaceSm) {
                DotIconButton(.back, title: "Back") {}
                DotIconButton(.close, title: "Close") {}
                Divider().frame(height: 18)
                DotIconButton(.search, title: "Search") {}
                DotIconButton(.settings, title: "Settings") {}
                Divider().frame(height: 18)
                DotIconButton(playing ? .pause : .play, title: playing ? "Pause" : "Play") {
                    playing.toggle()
                }
                DotIconButton(.pause, title: "Pause") {}
                    .disabled(true)
            }
            .tint(.primary)
            Divider()
            Text("Settings").font(.headline)
            DotSwitch("Notifications", isOn: $enabled)
            DotSwitch("Autoplay", isOn: $disabledSetting)
            Divider()
            HStack {
                Text("Right-to-left Back").font(.subheadline).foregroundStyle(.secondary)
                Spacer()
                DotIconButton(.back, title: "رجوع") {}
                    .environment(\.layoutDirection, .rightToLeft)
                    .tint(.primary)
            }
        }
        .padding(28)
        .frame(width: 450, height: 415, alignment: .topLeading)
        .background(Color(nsColor: .windowBackgroundColor))
        .tint(dark ? Color(red: 0.47, green: 0.78, blue: 0.92)
                   : Color(red: 0.09, green: 0.38, blue: 0.52))
    }
}

@main
struct RenderControls {
    static func main() throws {
        guard CommandLine.arguments.count == 2 else {
            throw CocoaError(.fileWriteInvalidFileName)
        }
        NSApplication.shared.setActivationPolicy(.prohibited)
        let artboard = HStack(spacing: 0) {
            ControlSpecimen(dark: false).environment(\.colorScheme, .light)
            ControlSpecimen(dark: true).environment(\.colorScheme, .dark)
        }
        let view = NSHostingView(rootView: artboard)
        let frame = NSRect(x: 0, y: 0, width: 900, height: 415)
        let window = NSWindow(contentRect: frame, styleMask: .borderless,
                              backing: .buffered, defer: false)
        window.contentView = view
        view.frame = frame
        view.layoutSubtreeIfNeeded()
        view.displayIfNeeded()
        guard let bitmap = view.bitmapImageRepForCachingDisplay(in: view.bounds) else {
            throw CocoaError(.fileWriteUnknown)
        }
        view.cacheDisplay(in: view.bounds, to: bitmap)
        guard let png = bitmap.representation(using: .png, properties: [:]) else {
            throw CocoaError(.fileWriteUnknown)
        }
        try png.write(to: URL(fileURLWithPath: CommandLine.arguments[1]))
    }
}
#endif
