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
            HStack(alignment: .top) {
                VStack(alignment: .leading, spacing: DotMetrics.spaceXs) {
                    Text("dot. controls").font(.system(size: 34, weight: .semibold))
                    Text(dark ? "Dark appearance" : "Light appearance")
                        .foregroundStyle(.secondary)
                }
                Spacer()
                Grid(horizontalSpacing: 5, verticalSpacing: 5) {
                    ForEach(0..<3) { row in
                        GridRow {
                            ForEach(0..<5) { column in
                                Circle().fill(.secondary.opacity(row + column < 5 ? 0.65 : 0.25))
                                    .frame(width: 3, height: 3)
                            }
                        }
                    }
                }
                .accessibilityHidden(true)
            }
            Divider()
            Text("Actions").font(.headline)
            HStack(spacing: DotMetrics.spaceSm) {
                DotIconButton(.back, title: "Back") {}
                DotIconButton(.close, title: "Close") {}
                DotIconButton(.search, title: "Search") {}
                DotIconButton(.settings, title: "Settings") {}
                DotIconButton(playing ? .pause : .play, title: playing ? "Pause" : "Play") {
                    playing.toggle()
                }
                DotIconButton(.pause, title: "Pause") {}
                    .disabled(true)
            }
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
            }
        }
        .padding(28)
        .frame(width: 450, height: 450, alignment: .topLeading)
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
        let frame = NSRect(x: 0, y: 0, width: 900, height: 450)
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
