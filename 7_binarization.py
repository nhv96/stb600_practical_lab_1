import cv2
import numpy as np

img = cv2.imread('images/tree.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
win1 = "Gray"

win2 = "Color"
cv2.namedWindow(win1)

cv2.namedWindow(win2)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Num contours:", len(contours))
c = max(contours, key=cv2.contourArea)

x,y,w,h = cv2.boundingRect(c)

# cv.minAreaRect returns:
# (center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(c)
rorect = cv2.minAreaRect(c)
box = cv2.boxPoints(rorect)
box = np.intp(box)

cv2.drawContours(img, [c], -1, (36, 255, 12), 2)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
cv2.rectangle(img, (x, y), ((x+w), (y+h)), color=(0,0,125), thickness=3)

angle = rorect[2]
width = int(rorect[1][0])
height = int(rorect[1][1])

if width < height:
    angle = 90-angle
else:
    angle = -angle
print("angle:", angle)

cv2.imshow(win2, img)
cv2.imshow(win1, gray)

cv2.waitKey(0)
cv2.destroyAllWindows()