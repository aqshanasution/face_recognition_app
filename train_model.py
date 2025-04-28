import cv2
import os
import numpy as np

dataset_path = 'dataset'
faces = []
labels = []

for filename in os.listdir(dataset_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(dataset_path, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        try:
            label = int(filename.split('_')[0])
            faces.append(img)
            labels.append(label)
        except:
            print(f"❌ Nama file tidak sesuai format label_nama: {filename}")

if len(faces) < 1:
    print("❌ Dataset minimal butuh 2 gambar untuk training.")
    exit()

faces = np.array(faces)
labels = np.array(labels)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, labels)
recognizer.save('trained_model.yml')

print("✅ Model training selesai & disimpan.")
