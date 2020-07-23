import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow("Tracker", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Tracker", 700, 240)
cv2.createTrackbar("Hue min", "Tracker", 0, 179, nothing)
cv2.createTrackbar("Hue max", "Tracker", 179, 179, nothing)
cv2.createTrackbar("Sat min", "Tracker", 0, 255, nothing)
cv2.createTrackbar("Sat max", "Tracker", 255, 255, nothing)
cv2.createTrackbar("Val min", "Tracker", 0, 255, nothing)
cv2.createTrackbar("Val max", "Tracker", 255, 255, nothing)

while True:
    img = cv2.imread('Resources/lamb.jpg')
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min", "Tracker")
    h_max = cv2.getTrackbarPos("Hue max", "Tracker")
    s_min = cv2.getTrackbarPos("Sat min", "Tracker")
    s_max = cv2.getTrackbarPos("Sat max", "Tracker")
    v_min = cv2.getTrackbarPos("Val min", "Tracker")
    v_max = cv2.getTrackbarPos("Val max", "Tracker")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("mast", mask)

    cv2.waitKey(1)


# show the image for 5 seconds, 0 means undefinite
# cv2.waitKey(10000)

# destroy all the image windows
# cv2.destroyAllWindows()
