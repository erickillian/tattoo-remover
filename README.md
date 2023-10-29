# Tattoo Remover

Easily remove tattoos from images of people using AI!

![Before and After](./animations/transition.gif)

## Features

- 🎨 Remove tattoos from any part of the body.
- 📸 Supports various image formats.
- 🚀 Fast processing using UNet

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/erickillian/tattoo-remover.git
   ```
2. Install python3

    see [https://www.python.org/downloads/](https://www.python.org/downloads/)

3. Install pytorch on your device

    see [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) for instructions on how to install pytorch on your device

4. Install python requirements for this project
    ```bash
    pip install -r requirements.txt
    ```

5. Download model weights (.safetensor) available on Huggingface
    
    available at [https://huggingface.co/erickillian/tattoo-removal](https://huggingface.co/erickillian/tattoo-removal/tree/main)
