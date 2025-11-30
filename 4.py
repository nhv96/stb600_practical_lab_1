import cv2
import numpy as np

img = cv2.imread('images/colormap.jpg', cv2.IMREAD_COLOR)

gc1 = img[:, :, 0]
gc2 = img[:, :, 1]
gc3 = img[:, :, 2]

gc = np.hstack([gc1, gc2, gc3])

cv2.imshow('Gray Channel', gc)
cv2.waitKey(0)

# want red
r = img.copy()
r[:, :, 0] = 0 # set blue to 0
r[:, :, 1] = 0 # set green to 0

# want green
g = img.copy()
g[:, :, 0] = 0 # set blue to 0
g[:, :, 2] = 0 # set red to 0

# want blue
b = img.copy()
b[:, :, 1] = 0 # set green to 0
b[:, :, 2] = 0 # set red to 0

cl = np.hstack([r, g, b])

cv2.imshow('Color Channel', cl)
cv2.waitKey(0)

cv2.destroyAllWindows()