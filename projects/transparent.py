
# pip install Pillow
from PIL import Image

image_path = "H:\\text_qr_code.png"
image = Image.open(image_path)
image = image.convert("RGBA")
data = list(image.getdata())

# Replace white pixels with transparent ones
new_data = []
for pixel in data:
    # Check if the pixel is white (R, G, B values are all 255)
    if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
        # Replace white pixel with transparent pixel (RGBA values are 0, 0, 0, 0)
        new_data.append((0, 0, 0, 0))
    else:
        # Keep the original pixel
        new_data.append(pixel)

# Update the image data with the new data
image.putdata(new_data)

# Save the image with transparent white pixels
image.save(image_path)
