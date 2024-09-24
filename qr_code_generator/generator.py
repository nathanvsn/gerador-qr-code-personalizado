import qrcode
from qrcode.image.styledpil import StyledPilImage
from PIL import Image
from typing import Optional
from .styles.marker_styles import MarkerStyle, MARKER_SVGS
from .styles.border_styles import BorderStyle, BORDER_SVGS
from .styles.line_styles import LineStyle, LINE_STYLES
from .utils.image_utils import svg_to_pil, add_center_image

class QRCodeGenerator:
    def create_custom_qr(
        self,
        data: str,
        size: int = 10,
        border: int = 4,
        marker_style: MarkerStyle = MarkerStyle.SQUARE,
        border_style: BorderStyle = BorderStyle.SQUARE,
        line_style: LineStyle = LineStyle.SQUARE,
        center_image: Optional[str] = None
    ) -> Image.Image:
        qr = qrcode.QRCode(
            version=7,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=border
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white",
            image_factory=StyledPilImage,
            module_drawer=LINE_STYLES[line_style]
        )
        img = img.convert("RGBA")

        marker_svg = MARKER_SVGS[marker_style]
        border_svg = BORDER_SVGS[border_style]
        
        border_img = svg_to_pil(border_svg, size * 7)
        center_img = svg_to_pil(marker_svg, size * 3)

        self._draw_custom_position_patterns(img, border_img, center_img, size, border)

        if center_image:
            add_center_image(img, center_image)

        return img

    def _draw_custom_position_patterns(
        self,
        img: Image.Image,
        border_img: Image.Image,
        center_img: Image.Image,
        size: int,
        border: int
    ) -> None:
        def draw_pattern(x: int, y: int) -> None:
            pattern = Image.new('RGBA', (size * 7, size * 7), (0, 0, 0, 0))
            pattern.paste(border_img, (0, 0), border_img)
            pattern.paste(center_img, (size * 2, size * 2), center_img)
            img.paste(pattern, (x, y), pattern)

        draw_pattern(border * size, border * size)  # Top-left
        draw_pattern(img.width - size * 7 - border * size, border * size)  # Top-right
        draw_pattern(border * size, img.height - size * 7 - border * size)  # Bottom-left
