# -----------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -----------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open("D:\كورس\Python with Elzero\Files\\image.jpg")

# Show The Image
# myImage.show()

# My Cropped Image (left, right, upper, lower)
myBox = (400, 0, 2650, 1600)
myNewImage = myImage.crop(myBox)

# Show New Image
# myNewImage.show()

# My Converted Mode Image 
myConverted = myImage.convert("L")
myConverted.show() # make image in black mode but the image is black already