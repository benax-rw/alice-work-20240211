import cv2
import os
import face_recognition

# Load the known face images and their names
known_faces = []
known_names = []
for filename in os.listdir('known_faces'):
    # Check if the file is an image
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        image = face_recognition.load_image_file('known_faces/Gabriel/' + filename)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(face_encoding)
        known_names.append(os.path.splitext(filename)[0])

# Initialize the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture device
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video stream
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Extract the face image from the frame
        face_image = frame[y:y+h, x:x+w]

        # Convert the face image to RGB format for face recognition
        face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

        # Try encoding the face image for face recognition
        try:
            face_encoding = face_recognition.face_encodings(face_image_rgb)[0]
        except IndexError:
            # If face encoding fails, skip this face
            continue

        # Compare the face encoding to the known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = 'Unknown'

        # Find the best match among the known faces
        face_distances = face_recognition.face_distance(known_faces, face_encoding)
        best_match_index = face_distances.argmin()
        if matches[best_match_index]:
            name = known_names[best_match_index]

        # Draw a rectangle around the face and label it with the person's name
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device
video_capture.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
