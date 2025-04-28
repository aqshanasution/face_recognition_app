import cv2

print(cv2.__version__)  # cek versi

recognizer = cv2.face.LBPHFaceRecognizer_create()
print("Recognizer berhasil dibuat!")
