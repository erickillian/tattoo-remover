from PIL import Image
from math import sqrt, ceil
import os

def square_like_concatenation(images):
    # Determine number of rows and columns for a square-like layout
    num_images = len(images)
    num_cols = ceil(sqrt(num_images))
    num_rows = ceil(num_images / num_cols)
    
    # Determine dimensions of the final concatenated image
    max_width_per_col = [0] * num_cols
    max_height_per_row = [0] * num_rows

    for idx, img in enumerate(images):
        row = idx // num_cols
        col = idx % num_cols
        max_width_per_col[col] = max(max_width_per_col[col], img.width)
        max_height_per_row[row] = max(max_height_per_row[row], img.height)

    total_width = sum(max_width_per_col)
    total_height = sum(max_height_per_row)
    combined = Image.new('RGB', (total_width, total_height))

    # Paste each image at its determined position
    x_offset, y_offset = 0, 0
    for idx, img in enumerate(images):
        row = idx // num_cols
        col = idx % num_cols
        combined.paste(img, (x_offset, y_offset))
        
        # Move offsets
        x_offset += max_width_per_col[col]
        if (idx + 1) % num_cols == 0:
            x_offset = 0
            y_offset += max_height_per_row[row]

    return combined

def image_transition(img1, img2, steps=10):
    frames = []

    image1 = Image.blend(img1, img2, 0)
    for i in range(steps):
        frames.append(image1)

    for step in range(steps + 1):
        alpha = step / steps
        blended = Image.blend(img1, img2, alpha)
        frames.append(blended)

    image2 = Image.blend(img1, img2, 1)
    for i in range(steps):
        frames.append(image2)

    for step in range(steps + 1):
        alpha = step / steps
        blended = Image.blend(img2, img1, alpha)
        frames.append(blended)

    return frames

def main(dir1, dir2, output_file):
    # List and sort image filenames from both directories
    image_filenames1 = sorted([img for img in os.listdir(dir1) if img.endswith(('.png', '.jpg', '.jpeg'))])
    image_filenames2 = sorted([img for img in os.listdir(dir2) if img.endswith(('.png', '.jpg', '.jpeg'))])

    # Load the sorted images
    images1 = [Image.open(f"{dir1}/{img}") for img in image_filenames1]
    images2 = [Image.open(f"{dir2}/{img}") for img in image_filenames2]

    if len(images1) != len(images2) or len(images1) == 0:
        print("The directories must have the same number of images and at least one image.")
        return

    concatenated1 = square_like_concatenation(images1)
    concatenated2 = square_like_concatenation(images2)

    all_frames = image_transition(concatenated1, concatenated2)
    
    all_frames[0].save(output_file, save_all=True, append_images=all_frames[1:], duration=100, loop=0)


if __name__ == "__main__":
    dir1 = "test_inputs"
    dir2 = "test_outputs"
    output_file = "transition.gif"
    main(dir1, dir2, output_file)
