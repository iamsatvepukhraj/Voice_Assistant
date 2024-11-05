import cv2

def play_intro_video():
    intro_video_path = r"C:\Users\admin\voice_assistant\intro.mp4"

    # Create a VideoCapture object
    cap = cv2.VideoCapture(intro_video_path)

    # Check if video file opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Create a window to display the video
    cv2.namedWindow("Intro Video", cv2.WINDOW_NORMAL)

    while True:
        # Read the video frame by frame
        ret, frame = cap.read()

        # If frame is read correctly, display it in the window
        if ret:
            cv2.imshow("Intro Video", frame)

            # Exit the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            # Break the loop if video is over or cannot be read
            break

    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()
