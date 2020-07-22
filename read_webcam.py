import cv2

# initiate the camera of the devide
cap = cv2.VideoCapture(0)

# define the size
cap.set(3, 640)
cap.set(4, 480)

# increase the brightness
cap.set(10, 200)

# check if the capture is open the show the video
while cap.isOpened():

    # Capture the response and frame
    ret, frame = cap.read()

    # if response is true run further
    if ret == True:

        # take the frame and flip false 0=true
        frame = cv2.flip(frame, 1)

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

