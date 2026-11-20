import SwiftUI

struct DotGlyph: Shape {
    let symbol: DotIconButton.Symbol

    func path(in rect: CGRect) -> Path {
        var lines = Path()
        var dots = Path()

        func dot(_ x: CGFloat, _ y: CGFloat) {
            dots.addEllipse(in: CGRect(x: x - 1.6, y: y - 1.6, width: 3.2, height: 3.2))
        }

        switch symbol {
        case .back:
            lines.addLines([CGPoint(x: 13, y: 5), CGPoint(x: 6, y: 12), CGPoint(x: 13, y: 19)])
            dot(18, 12)
        case .close:
            lines.addLines([CGPoint(x: 6, y: 6), CGPoint(x: 18, y: 18)])
            lines.addLines([CGPoint(x: 18, y: 6), CGPoint(x: 6, y: 18)])
        case .search:
            lines.addEllipse(in: CGRect(x: 4, y: 4, width: 12, height: 12))
            lines.addLines([CGPoint(x: 15, y: 15), CGPoint(x: 20, y: 20)])
        case .settings:
            // Each tooth has a flat outer edge and a short valley before the next tooth.
            let gear = (0..<32).map { point -> CGPoint in
                let angle = Double(point) * .pi / 16 - .pi / 32
                let radius: CGFloat = point % 4 < 2 ? 9 : 7.5
                return CGPoint(x: 12 + cos(angle) * radius, y: 12 + sin(angle) * radius)
            }
            lines.addLines(gear)
            lines.closeSubpath()
            dot(12, 12)
        case .play:
            lines.addLines([CGPoint(x: 6, y: 4), CGPoint(x: 19, y: 12), CGPoint(x: 6, y: 20)])
            lines.closeSubpath()
            dot(10.8, 12)
        case .pause:
            lines.addLines([CGPoint(x: 8, y: 5), CGPoint(x: 8, y: 19)])
            lines.addLines([CGPoint(x: 16, y: 5), CGPoint(x: 16, y: 19)])
        }

        var glyph = lines.strokedPath(StrokeStyle(lineWidth: 2.35, lineCap: .round, lineJoin: .round))
        glyph.addPath(dots)
        return glyph.applying(CGAffineTransform(a: rect.width / 24, b: 0,
                                                c: 0, d: rect.height / 24,
                                                tx: rect.minX, ty: rect.minY))
    }
}
