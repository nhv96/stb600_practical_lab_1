import cv2
import numpy as np
import time

# In OpenCV, finding contours is like finding white object from black background. 
# So remember, object to be found should be white and background should be black.

img = cv2.imread('images/piece05.png')
h, w = img.shape[:2]
img = cv2.resize(img, ((int(w/5), int(h/5))))

win_name = "Contours"

# convert to gray binary for easier detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow(win_name)

def nothing(x):
    pass

trackLowThres = "Lower Threshold"
cv2.createTrackbar(trackLowThres, win_name, 103, 255, nothing)

trackHighThres = "Higher Threshold"
cv2.createTrackbar(trackHighThres, win_name, 255, 255, nothing)

trackAvgKernel = "Avg Kernel"
cv2.createTrackbar(trackAvgKernel, win_name, 3, 30, nothing)

trackGausKernel = "Gaussian Kernel"
cv2.createTrackbar(trackGausKernel, win_name, 3, 30, nothing)

while True:
    # Hit Esc
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    lowTh = cv2.getTrackbarPos(trackLowThres, win_name)
    highTh = cv2.getTrackbarPos(trackHighThres, win_name)

    avgkernel = cv2.getTrackbarPos(trackAvgKernel, win_name)
    if avgkernel % 2 == 0:
        avgkernel = avgkernel+1

    gauskernel = cv2.getTrackbarPos(trackGausKernel, win_name)
    if gauskernel % 2 == 0:
        gauskernel = gauskernel+1

    # apply threshold
    ret, resultImg = cv2.threshold(gray, lowTh, highTh, 0)

    # remove noise by averaging
    resultImg = cv2.blur(resultImg, (avgkernel, avgkernel))

    # gaus
    resultImg = cv2.GaussianBlur(resultImg, (gauskernel, gauskernel), 0)

    resultImg = cv2.Canny(resultImg, 30, 200)
    # inverse the image
    # resultImg = 255 - resultImg

    contours, hierarchy = cv2.findContours(resultImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    txt = "Number of Contours found = " + str(len(contours))
    cv2.putText(resultImg, txt, (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 0, 0), 1, cv2.LINE_AA)

    cv2.imshow(win_name,  resultImg)
    time.sleep(0.1)

cv2.destroyAllWindows()