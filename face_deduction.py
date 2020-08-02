import cv2
import numpy as np

facaCascade = cv2.CascadeClassifier(
    'xmls/haarcascade_frontalface_default.xml')
# initiate the camera of the devide
cap = cv2.VideoCapture(0)

# define the size
cap.set(3, 640)
cap.set(4, 480)

# increase the brightness
cap.set(10, 200)

while cap.isOpened():

    # Capture the response and frame
    ret, frame = cap.read()

    # if response is true run further
    if ret == True:

        # take the frame and flip false 0=true
        frame = cv2.flip(frame, 1)

        faces = facaCascade.detectMultiScale(frame, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # show the video
        cv2.imshow("frame", frame)

        # press q to quit the video
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
# Release everything if job is finished
cap.release()

# destroy all the windows
cv2.destroyAllWindows()
