# Tattoo Remover

Easily remove tattoos from images of people using AI!

![Before and After](./animations/animation.gif)

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

5. Download trained model weights from (.safetensor) available on my huggingface account 
    
    available at [https://huggingface.co/erickillian/tattoo-removal](https://huggingface.co/erickillian/tattoo-removal/tree/main)

    And add model weights into directory

6. Add tattoo photos to test_inputs directory


## Usage

1. Run model on directory

    ```bash
    python3 run.py
    ```

2. Run image_blender.py to get animated transition between image pairs

    ```bash
    python3 image_blender.py
    ```

## Colab Integration

[<img src="https://colab.research.google.com/assets/colab-badge.svg" align="center">](https://colab.research.google.com/github/erickillian/tattoo-remover/blob/main/run.ipynb)

## Contribute

Currently the training data and process will remain closed source, however if there is enough interest that could change.

If you are interested in this project and would like to contribute please reach out!  **Email:** [erickill@usc.edu](mailto:erickill@usc.edu)


## License

[MIT](LICENSE.txt)

