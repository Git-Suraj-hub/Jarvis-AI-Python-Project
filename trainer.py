import cv2
import numpy as np
import os

# Path to the dataset
dataset_path = 'dataset'

# Initialize the recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to get images and labels from the dataset
def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []
    for image_path in image_paths:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        faces = face_cascade.detectMultiScale(img)
        for (x, y, w, h) in faces:
            face_samples.append(img[y:y+h, x:x+w])
            ids.append(int(os.path.split(image_path)[-1].split(".")[1]))
    return face_samples, ids

faces, ids = get_images_and_labels(dataset_path)
recognizer.train(faces, np.array(ids))
recognizer.save('recognizer/trainer.yml')
