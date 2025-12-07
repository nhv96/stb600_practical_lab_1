import cv2
import numpy as np
import time

# Image Moment is a particular weighted average of image pixel intensities, 
# with the help of which we can find some specific properties of an image, like radius, area, centroid etc. 
# To find the centroid of the image, we generally convert it to binary format and then find its center.

# To find the center of the blob, we will perform the following steps:
# 1. Convert the Image to grayscale.
# 2. Perform Binarization on the Image.
# 3. Find the center of the image after calculating the moments.

img = cv2.imread('images/star.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# binarize the image
_, bin_thres = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# find image moments
M = cv2.moments(bin_thres)

# find the center
cX = int(M["m10"]/M["m00"])
cY = int(M["m01"]/M["m00"])

cv2.circle(img, (cX, cY), 8, (255, 255, 255), -1)

cv2.imshow("Centroid", img)

cv2.waitKey(0)
cv2.destroyAllWindows()