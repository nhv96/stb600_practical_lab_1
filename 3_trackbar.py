import numpy as np
import cv2

img = cv2.imread("images/piece03.png", cv2.IMREAD_GRAYSCALE)
h, w = img.shape[:2]

win_name = "Threshold Adjuster"
# Create a window
cv2.namedWindow(win_name)

def nothing(x):
    pass

# --- Create Trackbars ---
# Trackbar for lower threshold
cv2.createTrackbar("Lower", win_name, 0, 255, nothing)

# Trackbar for upper threshold (max value)
cv2.createTrackbar("Upper", win_name, 255, 255, nothing)

resized = cv2.resize(img, (int(w/18), int(h/12)))

while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Read current trackbar positions
    low = cv2.getTrackbarPos("Lower", win_name)
    high = cv2.getTrackbarPos("Upper", win_name)

    # Apply threshold with live updated values
    _, th_binary = cv2.threshold(resized, low, high, cv2.THRESH_BINARY)
    _, th_binary_inv = cv2.threshold(resized, low, high, cv2.THRESH_BINARY_INV)
    _, th_trunc = cv2.threshold(resized, low, high, cv2.THRESH_TRUNC)
    _, th_tozero = cv2.threshold(resized, low, high, cv2.THRESH_TOZERO)
    _, th_tozero_inv = cv2.threshold(resized, low, high, cv2.THRESH_TOZERO_INV)
    images = [th_binary, th_binary_inv, th_trunc, th_tozero, th_tozero_inv]
    # Stack all results in a grid for comparison
    ii = np.hstack(images)
    cv2.imshow(win_name, ii)

cv2.destroyAllWindows()