import SwiftUI

/// A compact action for a familiar symbol. Supply a localized action name.
public struct DotIconButton: View {
    public enum Symbol: Sendable {
        case back, close, search, settings, play, pause
    }

    @Environment(\.layoutDirection) private var layoutDirection
    @ScaledMetric(relativeTo: .body) private var glyphSize = 26.0

    private let symbol: Symbol
    private let title: LocalizedStringKey
    private let action: () -> Void

    public init(_ symbol: Symbol, title: LocalizedStringKey, action: @escaping () -> Void) {
        self.symbol = symbol
        self.title = title
        self.action = action
    }

    public var body: some View {
        if #available(macOS 14, *) {
            button.buttonBorderShape(.capsule)
        } else {
            button
        }
    }

    private var button: some View {
        Button(action: action) {
            DotGlyph(symbol: symbol)
                .frame(width: glyphSize, height: glyphSize)
                .scaleEffect(x: symbol == .back && layoutDirection == .rightToLeft ? -1 : 1, y: 1)
                .accessibilityHidden(true)
                .frame(minWidth: DotMetrics.minimumTarget, minHeight: DotMetrics.minimumTarget)
                .contentShape(Rectangle())
        }
        .buttonStyle(.bordered)
        .accessibilityLabel(Text(title))
        .help(Text(title))
    }
}

/// A settings switch whose label names what it controls.
public struct DotSwitch: View {
    private let title: LocalizedStringKey
    @Binding private var isOn: Bool

    public init(_ title: LocalizedStringKey, isOn: Binding<Bool>) {
        self.title = title
        self._isOn = isOn
    }

    public var body: some View {
        Toggle(title, isOn: $isOn)
            .toggleStyle(.switch)
    }
}
