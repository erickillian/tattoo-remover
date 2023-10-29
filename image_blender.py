from PIL import Image
import os

def side_by_side_concatenation(images):
    total_width = sum(img.width for img in images)
    max_height = max(img.height for img in images)
    
    combined = Image.new('RGB', (total_width, max_height))
    
    x_offset = 0
    for img in images:
        combined.paste(img, (x_offset, 0))
        x_offset += img.width
        
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

    concatenated1 = side_by_side_concatenation(images1)
    concatenated2 = side_by_side_concatenation(images2)

    all_frames = image_transition(concatenated1, concatenated2)
    
    all_frames[0].save(output_file, save_all=True, append_images=all_frames[1:], duration=100, loop=0)


if __name__ == "__main__":
    dir1 = "test_inputs"
    dir2 = "test_outputs"
    output_file = "transition.gif"
    main(dir1, dir2, output_file)
