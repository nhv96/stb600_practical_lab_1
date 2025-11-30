import cv2
import numpy as np

img = cv2.imread('images/colormap.jpg')

def getrgb(x, y):
    b,g,r = img[y, x]
    return [int(r), int(g), int(b)]

print("Point 1", getrgb(400, 20))
print("Point 2", getrgb(232, 125))
print("Point 3", getrgb(400, 300))
print("Point 4", getrgb(140, 340))

# Point 1 RGB: [0, 0, 203]
# Point 2 RGB: [0, 254, 254]
# Point 3 RGB: [255, 103, 154]
# Point 4 RGB: [152, 203, 0]