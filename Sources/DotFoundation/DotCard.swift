import SwiftUI

public struct DotCard<Content: View>: View {
    private let content: Content

    public init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }

    public var body: some View {
        content
            .font(.body)
            .padding(DotMetrics.spaceMd)
            .background(.regularMaterial, in: RoundedRectangle(cornerRadius: DotMetrics.radiusCard))
    }
}

public struct DotActionStyle: ButtonStyle {
    public init() {}

    public func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.body.weight(.semibold))
            .padding(.horizontal, DotMetrics.spaceMd)
            .frame(minHeight: DotMetrics.minimumTarget)
            .background(.quaternary, in: RoundedRectangle(cornerRadius: DotMetrics.radiusControl))
            .opacity(configuration.isPressed ? 0.78 : 1)
    }
}
