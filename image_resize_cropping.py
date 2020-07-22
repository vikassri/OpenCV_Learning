import cv2
import numpy as np

# Reading the image
img = cv2.imread("Resources/bird.jpg")

######################  IMAGE RESIZE #################
# find the size of the images
print(img.shape)
"""
(1333, 2000, 3)  # width, height and channel
"""
# resize the image size
imgResize = cv2.resize(img, (640, 480))

# print the new image size
print(imgResize.shape)
"""
(480, 640, 3)  # width, height and channel
"""
# writing this image into new file
cv2.imwrite("Resources/small_birld.jpg", imgResize)

# showing the small image
cv2.imshow("Small Size", imgResize)

######################  IMAGE CROPPING #################

ImgCropped = imgResize[0:480, 200:640]  # [height, width]
cv2.imshow("Cropped Size", ImgCropped)


# waiting for the key or 10 secs
cv2.waitKey(10000)

# Destroy all the windows
cv2.destroyAllWindows()
