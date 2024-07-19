from tkinter import Tk, Text, Button, Label, filedialog
from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text, font_size):
    try:
        # Define image size and background color
        background_color = (255, 255, 255)
        text_color = (0, 0, 0)
        
        # Load a font
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        # Create a temporary image to calculate text size
        temp_image = Image.new('RGB', (1, 1), background_color)
        draw = ImageDraw.Draw(temp_image)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Define image size based on text size
        image_width = text_width + 40  # Add padding
        image_height = text_height + 40  # Add padding
        
        # Create a new image with white background
        image = Image.new('RGB', (image_width, image_height), background_color)
        draw = ImageDraw.Draw(image)
        
        # Calculate text position
        text_x = 20
        text_y = 20
        
        # Draw text on image
        draw.text((text_x, text_y), text, font=font, fill=text_color)
        
        return image
    except Exception as e:
        print(f"Error creating image: {e}")
        return None

def save_image():
    text = entry_text.get("1.0", "end-1c")  # Get all text from the Text widget
    font_size = 40  # Set font size
    image = create_image_with_text(text, font_size)
    if image:
        try:
            # Ask user where to save the image
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("All files", "*.*")])
            if file_path:
                image.save(file_path)
                status_label.config(text=f"Image saved successfully at {file_path}")
            else:
                status_label.config(text="Save operation canceled")
        except Exception as e:
            status_label.config(text=f"Error saving image: {e}")
    else:
        status_label.config(text="Error creating image")

# Tkinter setup
root = Tk()
root.title("Text to Image")

# Set large dimensions for the text widget
entry_text = Text(root, wrap="word", height=20, width=50)  # Adjusted text widget size
entry_text.pack(pady=10)

save_button = Button(root, text="Save Image", command=save_image)
save_button.pack(pady=5)

status_label = Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
