import cv2


def showVideo(video):
    # initiate the video
    cap = cv2.VideoCapture(video)

    # check if the capture is open the show the video
    while cap.isOpened():

        # Capture the response and frame
        success, frame = cap.read()

        # if response is true run further
        if success == True:

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


if __name__ == "__main__":
    video = "Resources/peoples.mp4"
    showVideo(video)
