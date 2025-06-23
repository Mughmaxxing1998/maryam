import os
from PIL import Image

def split_image_into_grid(image_path, output_folder='output_tiles'):
    """
    Splits an image into a 4x4 grid (16 tiles) and saves them with sequential numbering.

    Args:
        image_path (str): The path to the input image file.
        output_folder (str): The folder where the output tiles will be saved.
    """
    try:
        # Open the input image
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Calculate the width and height of each tile
        # Integer division is used to ensure whole pixel values
        tile_width = img_width // 4
        tile_height = img_height // 4

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Created directory: {output_folder}")

        # Initialize a counter for the filenames
        tile_number = 1

        # Iterate over rows
        for i in range(4):
            # Iterate over columns
            for j in range(4):
                # Calculate the coordinates for the crop box
                left = j * tile_width
                top = i * tile_height
                # To handle images where dimensions are not perfectly divisible by 4,
                # the right and bottom coordinates extend to the next tile's start
                right = (j + 1) * tile_width
                bottom = (i + 1) * tile_height

                # Crop the image to get the tile
                tile = img.crop((left, top, right, bottom))

                # Determine the output filename
                # The format is PNG to preserve transparency
                output_filename = os.path.join(output_folder, f"{tile_number}.png")

                # Save the tile
                tile.save(output_filename)
                print(f"Saved tile: {output_filename}")

                # Increment the tile number
                tile_number += 1

        print("\nImage splitting complete. 16 tiles saved.")

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    # --- IMPORTANT ---
    # Replace 'image_21e4e2.png' with the actual path to your image file.
    # If the image is not in the same directory as the script, provide the full path.
    # For example: 'C:/Users/YourUser/Pictures/my_photo.jpg' on Windows
    # or '/home/user/images/my_photo.png' on Linux/macOS.
    input_image = 'lobstar.jpg'  # Path to the input image file

    # You can change the name of the output folder if you like
    output_directory = 'split_images'

    # Call the function to split the image
    split_image_into_grid(input_image, output_directory)
