import cv2
import numpy as np

# load the images
img = cv2.imread("Resources/small_bird.jpg",)

# Convert the image into gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('Resources/birdg.jpg', imgGray)
