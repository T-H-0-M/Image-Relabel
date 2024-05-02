import os
import shutil
from pathlib import Path


def rename_and_move_images(input_dir, output_dir, start_number=0):
    """
    Renames and moves all images from the input directory and its subdirectories to the output directory,
    starting from the specified number.

    Parameters:
    input_dir (str): The directory to search for images.
    output_dir (str): The directory where the renamed images will be saved.
    start_number (int): The starting number for naming images.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    image_formats = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

    current_number = start_number

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(image_formats):
                file_path = os.path.join(root, file)
                new_filename = f"{current_number:06d}{Path(file).suffix}"
                output_path = os.path.join(output_dir, new_filename)

                shutil.move(file_path, output_path)
                print(f"Moved and renamed {file_path} to {output_path}")

                current_number += 1


input_directory = "./input"
output_directory = "./output"
start_num = 0

rename_and_move_images(input_directory, output_directory, start_num)
