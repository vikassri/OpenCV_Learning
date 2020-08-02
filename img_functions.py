import cv2
import numpy as np

# load the images
img = cv2.imread("Resources/small_bird.jpg",)

# Convert the image into gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the images using gaussianBlur
# ksize is kernal size, should always in odd, 1 is min and x is max
imgBlur = cv2.GaussianBlur(imgGray, ksize=(15, 15), sigmaX=0)

# Deduct the edge of images, you can increase the threshold to reduce the edge deduction
imgCanny = cv2.Canny(img, threshold1=100, threshold2=100)

# Increase the thickness of edges introduce the dialation, required numpy to use matrix
imgkernal = np.ones((5, 5), np.uint8)
imgDialtion = cv2.dilate(imgCanny, kernel=imgkernal, iterations=1)

# Erode is opposide of dialtion, we decrease the thikness of Canny
imgErode = cv2.erode(imgDialtion, kernel=imgkernal, iterations=1)

# showing the images
cv2.imshow("Color Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Edge Deducted Image", imgCanny)
cv2.imshow("Dialated Image", imgDialtion)
cv2.imshow("Erode Image", imgErode)

# show the image for 5 seconds, 0 means undefinite
cv2.waitKey(30000)

# destroy all the image windows
cv2.destroyAllWindows()
