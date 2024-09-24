from qr_code_generator.generator import QRCodeGenerator
from qr_code_generator.styles.marker_styles import MarkerStyle
from qr_code_generator.styles.border_styles import BorderStyle
from qr_code_generator.styles.line_styles import LineStyle

if __name__ == "__main__":
    qr_generator = QRCodeGenerator()
    qr_img = qr_generator.create_custom_qr(
        "https://www.exemplo.com",
        size=10,
        border=4,
        marker_style=MarkerStyle.PLUS,
        border_style=BorderStyle.CIRCLE,
        line_style=LineStyle.ROUNDED,
        center_image="scan-me-frame.png"
    )
    qr_img.save("custom_qr_code_with_svg.png")
    qr_img.show()