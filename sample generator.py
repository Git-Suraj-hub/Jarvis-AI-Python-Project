import cv2
import os

# Initialize the camera
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set video frame width
cam.set(4, 480)  # Set video frame height

# Load the Haar Cascade face detection model
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Prompt for user ID
face_id = input("Enter a numeric user ID here: ")
print("Taking samples, look at the camera...")

# Initialize sample face count
count = 0

# Create a directory to save the captured images
if not os.path.exists('dataset'):
    os.makedirs('dataset')

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        # Save the captured image into the dataset folder
        cv2.imwrite(f"dataset/User.{face_id}.{count}.jpg", gray[y:y+h, x:x+w])

    cv2.imshow('image', img)

    # Break the loop if 'q' is pressed or 30 images are taken
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 30:
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
