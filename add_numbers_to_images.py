from PIL import Image, ImageDraw, ImageFont
import os

def add_numbers_to_images():
    image_dir = "static/split_images/"
    font_size = 50  # Adjusted font size
    text_color_with_alpha = (0, 0, 0, 128)  # Black with 50% opacity (0-255)

    # Try to load a common system font, fall back if not found
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Common on Linux
        "/Library/Fonts/Arial.ttf",  # Common on macOS
        "arial.ttf" # Common on Windows, or if installed locally
    ]

    font = None
    for path in font_paths:
        try:
            font = ImageFont.truetype(path, font_size)
            break
        except IOError:
            continue

    if font is None:
        try:
            font = ImageFont.load_default(size=font_size) # Use a larger default font
            print("Default font loaded as fallback.")
        except AttributeError: # For older Pillow versions that don't support size in load_default
             font = ImageFont.load_default()
             print("Basic default font loaded as fallback.")


    for i in range(1, 17): # Iterate from 1.png to 16.png
        filename = f"{i}.png"
        filepath = os.path.join(image_dir, filename)

        if not os.path.exists(filepath):
            print(f"File {filepath} not found, skipping.")
            continue

        try:
            img = Image.open(filepath).convert("RGBA")
            draw = ImageDraw.Draw(img)

            text = str(i)

            # Calculate text bounding box using textbbox
            try:
                # Pillow >= 8.0.0
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
            except AttributeError:
                # Pillow < 8.0.0
                text_width, text_height = draw.textsize(text, font=font)


            # Position for top-left corner with some padding
            x = 10
            y = 10

            # Simple background rectangle for better visibility if needed
            # rect_x0 = x - 5
            # rect_y0 = y - 5
            # rect_x1 = x + text_width + 5
            # rect_y1 = y + text_height + 5
            # draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill=(255, 255, 255, 100))


            draw.text((x, y), text, font=font, fill=text_color_with_alpha)

            img.save(filepath)
            print(f"Processed {filepath}")

        except Exception as e:
            print(f"Could not process {filepath}: {e}")

if __name__ == "__main__":
    add_numbers_to_images()
