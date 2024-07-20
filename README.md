# Text-to-Image Converter

This Tkinter application converts text into an image and allows you to save it as a PNG file. It uses the Pillow library for image creation and manipulation.

## Features

- **Text Input**: Enter and edit text in a large text widget.
- **Image Generation**: Converts text into an image with a customizable font size.
- **Save Functionality**: Save the generated image as a PNG file through a file dialog.
- **Error Handling**: Provides feedback if image creation or saving fails.

## Requirements

- **Python 3.x**
- **Tkinter** (usually included with Python)
- **Pillow** (Python Imaging Library fork)

# To install the required Python package, run:

pip install pillow
<br>
# Usage
Clone the Repository:
Clone this repository to your local machine using:
git clone https://github.com/parvathamramcharan/Text_to_Image_Converter
<br>
Run the Application:
Navigate to the project directory and execute:
python text_to_image_converter.py


Enter Text:
Type or paste the text you want to convert into the text widget.

Save Image:
Click the "Save Image" button to open a file dialog. Choose where to save the PNG image.

Check Status:
The status label will update with information about the operation's success or failure.

## Code Overview
create_image_with_text(text, font_size):
Generates an image from the text with the specified font size and adds padding.
<br>
save_image():
Retrieves text from the widget, creates the image, and saves it via a file dialog.
<br>
Tkinter Setup:
Configures the main window with a text widget, save button, and status label.

# Acknowledgments
Built with Tkinter and Pillow.


