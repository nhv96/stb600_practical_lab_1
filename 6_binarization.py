import cv2
import numpy as np
import time

img = cv2.imread('images/star.png', cv2.IMREAD_GRAYSCALE)

win_name = 'Star - Binarization filter'
cv2.namedWindow(win_name)

