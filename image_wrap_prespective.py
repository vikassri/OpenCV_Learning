import cv2
import numpy as np

img = cv2.imread('Resources/k_cards.jpg')

# set the width and height of perspective
width, height = 250, 350

# pt1 have upper left, upper right, lower left, lower right
pt1 = np.float32([[298, 339], [529, 416], [131, 650], [384, 741]])

# pt2 have the perception we want for the image
pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# get the perspective of our cordinates to actual cordinates
matrix = cv2.getPerspectiveTransform(pt1, pt2)

# wrap into output to see the Images into correct perspective
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# show image
cv2.imshow("Image", img)
cv2.imshow("Changed Image", imgOutput)

# show the image for 5 seconds, 0 means undefinite
cv2.waitKey(10000)

# destroy all the image windows
cv2.destroyAllWindows()
