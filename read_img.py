import os, sys
import cv2
import numpy as np

if __name__ == "__main__":
    # print(cv2.__version__)
    # read the image from the path {option 1=coloured, 0=grayed, -1=unchanged}
    img = cv2.imread("Resources/bird.jpg", -1,)

    # show the images
    cv2.imshow("output", img)

    # show the image for 5 seconds, 0 means undefinite
    cv2.waitKey(5000)

    # destroy all the image windows
    cv2.destroyAllWindows()

    # Write the img into new file
    cv2.imwrite("new_image.png", img)

