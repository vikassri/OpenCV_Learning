import cv2
import numpy as np
from img_joining_2 import stackImages


def getContours(img):
    contours, chy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # draw outer line of the shapes
        cv2.drawContours(imgContour, contours=cnt,
                         contourIdx=-1, color=(255, 0, 0), thickness=3)

        # Perimeter of shapes closed is true becoz all the shaped are closed one
        perimeter = cv2.arcLength(curve=cnt, closed=True)
        # approximate aread of shapes
        approx = cv2.approxPolyDP(
            curve=cnt, epsilon=0.02*perimeter+2, closed=True)
        # sides/corners of objects
        x, y, w, h = cv2.boundingRect(approx)

        # get the shape of shapes
        if len(approx) == 8:
            objType = "circle"
        elif len(approx) == 3:
            objType = "Tri"
        elif len(approx) == 4:
            if .95 < w/float(h) < 1.05:
                objType = "square"
            else:
                objType = "Rect"
        elif len(approx) == 5:
            objType = "poly"
        elif len(approx) == 6:
            objType = "hexa"
        else:
            objType = "Unknown"

        # create rectangle around the shapes
        cv2.rectangle(imgContour, pt1=(x, y), pt2=(
            x+w, y+h), color=(0, 255, 0), thickness=3)

        # add text to shapes
        cv2.putText(imgContour, objType, org=(x+(w//2)-20, y+(h//2)),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0, 0, 0), thickness=2)


# reading the shape
img = cv2.imread('Resources/shapes.jpg')
imgContour = img.copy()

# convert into gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur Image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

# Deduct edges
imgCanny = cv2.Canny(imgBlur, 50, 50)

# Blank Image
imgBlank = np.zeros_like(img)

# get Contours
getContours(imgCanny)

# show images
stackImages([img, imgGray, imgBlur], [imgContour, imgCanny, imgBlank])

# show the image for 5 seconds, 0 means undefinite
cv2.waitKey(10000)

# destroy all the image windows
cv2.destroyAllWindows()
