import SwiftUI

/// A compact action for a familiar symbol. Supply a localized action name.
public struct DotIconButton: View {
    public enum Symbol: Sendable {
        case back, close, search, importFiles, settings, play, pause

        public var systemName: String {
            switch self {
            case .back: return "chevron.backward"
            case .close: return "xmark"
            case .search: return "magnifyingglass"
            case .importFiles: return "square.and.arrow.down"
            case .settings: return "gearshape"
            case .play: return "play.fill"
            case .pause: return "pause.fill"
            }
        }
    }

    @ScaledMetric(relativeTo: .body) private var glyphSize = 21.0

    private let symbol: Symbol
    private let title: LocalizedStringKey
    private let action: () -> Void

    public init(_ symbol: Symbol, title: LocalizedStringKey, action: @escaping () -> Void) {
        self.symbol = symbol
        self.title = title
        self.action = action
    }

    public var body: some View {
        Button(action: action) {
            Label(title, systemImage: symbol.systemName)
                .labelStyle(.iconOnly)
                .font(.system(size: glyphSize, weight: .medium))
                .frame(minWidth: DotMetrics.minimumTarget, minHeight: DotMetrics.minimumTarget)
                .contentShape(Rectangle())
        }
        .buttonStyle(.borderless)
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
