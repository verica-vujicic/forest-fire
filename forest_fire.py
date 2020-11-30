"""
This program will highlight the sufficiently red pixels 
and grayscale all other pixels in the image so the area
covered in a fire would be highlighted.
"""

# Pillow package have to be installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'greenland-fire.png'

def find_flames(filename):
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.blue + pixel.green)//3
        if pixel.red >= average:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.red = average
            pixel.blue = average
            pixel.green = average
    return image

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()

    
def get_file():
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
