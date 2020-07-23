import cv2
import numpy as np


# img = cv2.imread("Resources/small_bird.jpg")

# Create black image, add 3 will provide color
img = np.zeros((512, 512, 3), np.uint8)

# change the color to blue
img[:] = 255, 0, 0

# small part of img to blue, gree, red
img[0:125, 0:] = 255, 0, 0
img[150:320, 0:] = 0, 255, 0
img[320:512, 0:] = 0, 0, 255

# line on image
cv2.line(img, pt1=(0, 0), pt2=(512, 512), color=(255, 255, 255), thickness=3)
# same with using shape method
cv2.line(
    img,
    pt1=(0, 0),
    pt2=(img.shape[1], img.shape[0]),
    color=(255, 255, 255),
    thickness=3,
)

# rectangle
cv2.rectangle(img, pt1=(0, 0), pt2=(300, 300), color=(200, 200, 200), thickness=2)

# circle
cv2.circle(img, center=(300, 300), radius=50, color=(100, 100, 100), thickness=2)

# text
cv2.putText(
    img,
    text="Sample Text",
    org=(100, 100),
    fontFace=cv2.FONT_HERSHEY_PLAIN,
    fontScale=2,
    color=(255, 255, 255),
    thickness=3,
)

cv2.imshow("Image", img)

# show the image for 5 seconds, 0 means undefinite
cv2.waitKey(10000)

# destroy all the image windows
cv2.destroyAllWindows()
