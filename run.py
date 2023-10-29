import torch
import os
from PIL import Image
from model import UNet
from torchvision import transforms
from torchvision.utils import save_image
from safetensors.torch import load_model

image_transforms = transforms.Compose(
    [
        transforms.Resize(512),
        transforms.CenterCrop(512),
        transforms.ToTensor(),
    ]
)

# Gets the best device to load the model to
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model
model = UNet()
model.to(device)
model.eval()
load_model(model, "tattoo_remover.safetensors")

input_dir = "test_inputs"
output_dir = "./test_outputs"
os.makedirs(output_dir, exist_ok=True)

# Process each image in the directory
for img_file in os.listdir(input_dir):
    if img_file.endswith(('.jpg', '.jpeg', '.png')):  # Add other formats if needed
        image_path = os.path.join(input_dir, img_file)
        full_path = os.path.join(os.getcwd(), image_path)
        image = Image.open(full_path)
        input = image_transforms(image)
        input = torch.unsqueeze(input, 0)

        # Forward the image through the model
        with torch.no_grad():
            input = input.to(device)
            output = model(input)

        # Saves the input-output result concatenated together
        output_path = os.path.join(output_dir, img_file)
        save_image(output, output_path)
        print(f"Saved {output_path}")
