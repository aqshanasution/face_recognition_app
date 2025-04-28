import cv2
import os
import numpy as np
import datetime
import subprocess

# Cek apakah recognizer tersedia
if not hasattr(cv2, 'face'):
    raise Exception("OpenCV face module tidak tersedia. Pastikan install opencv-contrib-python.")

# Load model awal (biar tetap bisa detect known)
model_path = 'trained_model.yml'
if os.path.exists(model_path):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(model_path)
else:
    recognizer = cv2.face.LBPHFaceRecognizer_create()

cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

# Folder dataset dan unknown
dataset_dir = 'dataset'
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

captured_unknown_faces = []
human_counter = len(os.listdir(dataset_dir)) + 1  # lanjut dari terakhir

print("Tekan ESC untuk keluar.")

def retrain_model():
    print("Retrain model dimulai...")
    subprocess.run(["python", "train_model.py"])
    print("Retrain model selesai.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]

        try:
            id, confidence = recognizer.predict(face_img)
        except:
            id, confidence = -1, 100

        if confidence < 60:
            text = f"User ID {id} ({round(100 - confidence, 2)}%)"
        else:
            text = "Unknown"
            is_new_face = True

            for saved_face in captured_unknown_faces:
                saved_face_resized = cv2.resize(saved_face, (face_img.shape[1], face_img.shape[0]))
                diff = cv2.norm(face_img, saved_face_resized, cv2.NORM_L2)

                if diff < 2000:
                    is_new_face = False
                    break

            if is_new_face:
                filename = os.path.join(dataset_dir, f"0_human_{human_counter}.jpg")
                cv2.imwrite(filename, face_img)
                print(f"Wajah unknown baru disimpan: {filename}")
                captured_unknown_faces.append(face_img.copy())
                human_counter += 1

                retrain_model()

                # Reload recognizer setelah retrain
                recognizer.read(model_path)

        cv2.putText(frame, text, (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
