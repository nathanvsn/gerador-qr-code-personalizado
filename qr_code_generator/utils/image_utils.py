import cairosvg
from PIL import Image
import io

def svg_to_pil(svg_string: str, size: int) -> Image.Image:
    png_data = cairosvg.svg2png(bytestring=svg_string.encode('utf-8'), output_width=size, output_height=size)
    img = Image.open(io.BytesIO(png_data))
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    return img

def add_center_image(img: Image.Image, center_image: str) -> None:
    center_img = Image.open(center_image)
    center_size = min(img.width, img.height) // 3
    center_img = center_img.resize((center_size, center_size), Image.LANCZOS)

    background = Image.new("RGBA", center_img.size, (255, 255, 255, 255))
    background.paste(center_img, (0, 0), center_img if center_img.mode == 'RGBA' else None)

    padding_top = 0
    center_pos = ((img.width - center_size) // 2, (img.height - center_size) // 2 - padding_top)
    img.paste(background, center_pos, background)
