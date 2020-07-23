import cv2
import numpy as np
"""
We will be joining the images into horizontal and vertical stack

Requirement:
All the images should be of same channel and format like RBG, Gray or BW

Solution:
Before stacking we can convert them into same channel stack it

"""
# reading the image
img = cv2.imread('Resources/small_bird.jpg')

# Horizontal stack
imgHorizontalStack = np.hstack((img, img))

# Vertical Stack
imgVerticalStack = np.vstack((img, img))

# show image
cv2.imshow("Hortizontal Stack Image", imgHorizontalStack)
cv2.imshow("Vertical Stack Image", imgVerticalStack)

# show the image for 5 seconds, 0 means undefinite
cv2.waitKey(10000)

# destroy all the image windows
cv2.destroyAllWindows()
