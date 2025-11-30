import cv2
import numpy as np
import time

img = cv2.imread('images/star.png', cv2.IMREAD_GRAYSCALE)

win_name = 'Star - Canny filter'
cv2.namedWindow(win_name)

def nothing(x):
    pass

trackMinVal = "Min Val"
cv2.createTrackbar(trackMinVal, win_name, 30, 200, nothing)

trackMaxVal = "Max Val"
cv2.createTrackbar(trackMaxVal, win_name, 200, 255, nothing)

while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    minVal = cv2.getTrackbarPos(trackMinVal, win_name)
    maxVal = cv2.getTrackbarPos(trackMaxVal, win_name)

    resultImg = cv2.Canny(img, minVal, maxVal)

    contours, hierarchy = cv2.findContours(resultImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]

    M = cv2.moments(cnt)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    resultImg = cv2.circle(resultImg, (cx, cy), 5, (255, 255, 255), 3)

    resultImg = cv2.drawContours(resultImg, contours, 0, (255, 0, 0), 3)

    txt = "Contours = " + str(len(contours))
    cv2.putText(resultImg, txt, (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 0, 0), 1, cv2.LINE_AA)

    cv2.imshow(win_name,  resultImg)
    time.sleep(0.2)

cv2.destroyAllWindows()
