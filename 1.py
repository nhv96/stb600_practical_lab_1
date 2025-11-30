import cv2
import numpy as np

img = cv2.imread('images/Original.png')

print("Shape", img.shape)
print("Dtype", img.dtype)
print("Min", img.min(),"Max", img.max())
print("Size", img.size)
print("Dimension", img.ndim)

# There is a property in Original.png that has been automatically added by the CV2.imread function. 
# Find the property using the CV2.imread function. What is the property and how does it affect the information in the image?

# By default, `imread` load image with only 3 channels, ignoring Alpha channel and the image is left with RGB channels.
# Without alpha channel, the image lose the transparency data, meaning any pixel in the image that could have been transparent, now become opaque.