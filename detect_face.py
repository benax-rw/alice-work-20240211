import cv2

# Load the pre-trained face detection classifier from OpenCV's data directory
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start capturing video from the default camera
videoCapture = cv2.VideoCapture(0)

count = 1

while True:
    # Read a frame from the video stream
    ret, frame = videoCapture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame using the classifier
    # The scaleFactor, minNeighbors, and minSize parameters can be adjusted for better performance
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    # Draw rectangles around the detected faces on the original frame
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Slice the face from the frame and save it as an individual image
        face = frame[y:y+h, x:x+w]
        filename = "known_faces/Gabriel/Gabriel_" + str(count) + ".jpg"
        cv2.imwrite(filename, face)
        print("[INFO] Image " + filename + " saved.")
        count += 1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
videoCapture.release()
cv2.destroyAllWindows()
