import cv2
import numpy as np


# reading the image
img = cv2.imread('Resources/lamb.jpg')

# Convert the Image in to HSM
"""
For HSV, hue range is [0,179], saturation range is [0,255], and value range is [0,255]
"""
# finding the lower and upper bound
# https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv/48367205#48367205

lower = np.array([55, 52, 60], np.uint8)
upper = np.array([95, 250, 255], np.uint8)

# conver the im HSV format
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Final Image with Masking the color
imgMask = cv2.inRange(imgHSV, lower, upper)

# Merge Black and wite with original image and get the color img
imgResult = cv2.bitwise_and(img, img, mask=imgMask)

# show image
cv2.imshow("Image", img)
cv2.imshow("HSV Image", imgHSV)
cv2.imshow("Mask Image", imgMask)
cv2.imshow("Color Image", imgResult)


# show the image for 5 seconds, 0 means undefinite
cv2.waitKey(10000)

# destroy all the image windows
cv2.destroyAllWindows()
