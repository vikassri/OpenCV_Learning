import cv2
import numpy as np


img = cv2.imread('Resources/cards.jpg')

x1=44
y1=25

# first row
cv2.rectangle(img,(x1,y1),(426,550),color=(255,0,0),thickness=3)
cv2.rectangle(img,(426+x1,y1),(426*2-5,550),color=(0,255,0),thickness=3)

# second row
cv2.rectangle(img,(426+x1,550+y1),(426*2-5,550*2+5),color=(255,0,0),thickness=3)
cv2.rectangle(img,(x1,550+y1),(426,550*2+1),color=(0,255,0),thickness=3)


# show image
cv2.imshow("Image", img)

# show the image for 5 seconds, 0 means undefinite
cv2.waitKey(10000)

# destroy all the image windows
cv2.destroyAllWindows()
