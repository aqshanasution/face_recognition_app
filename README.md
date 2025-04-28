# 🤳 Aplikasi Pengenalan Wajah Real-time dengan Auto-Retrain 🔄

Proyek ini adalah aplikasi pengenalan wajah real-time 🚀 yang menggunakan OpenCV. Fitur utama dari aplikasi ini adalah kemampuannya untuk secara otomatis menyimpan wajah yang tidak dikenal 🤔 dan melakukan *retrain* model secara langsung 🧠.

## ✨ Fitur Utama

* **👀 Deteksi Wajah Real-time:** Menggunakan *Haar Cascade Classifier* untuk mendeteksi wajah dalam *feed* video dari kamera 📹.
* **👤 Pengenalan Wajah:** Menggunakan algoritma *Local Binary Patterns Histograms (LBPH)* untuk mengenali wajah yang sudah dikenal ✅.
* **💾 Penyimpanan Wajah Tidak Dikenal:** Secara otomatis menyimpan gambar wajah yang tidak dikenali ke dalam folder `dataset` 📂.
* **🔄 Auto-Retrain Model:** Setelah wajah baru disimpan, model pengenalan wajah secara otomatis dilatih ulang 🏋️ untuk memasukkan identitas baru.
* **🏷️ Pelabelan Sederhana:** Gambar wajah di folder `dataset` diharapkan memiliki format nama file `label_namafile.jpg` (contoh: `0_human_1.jpg`). Label `0` digunakan untuk wajah yang awalnya tidak dikenal dan ditambahkan melalui proses auto-retrain.

## 📂 Struktur Direktori
face_recognition_app/
├── dataset/
│   ├── 0_human_1.jpg
│   ├── 0_human_2.jpg
│   └── ...
├── haarcascade_frontalface_default.xml
├── main_with_autotrain.py
├── test_cv2_face.py
├── train_model.py
└── trained_model.yml

* `dataset/`: Direktori yang menyimpan gambar-gambar wajah untuk pelatihan 🖼️.
* `haarcascade_frontalface_default.xml`: File *Haar Cascade Classifier* untuk deteksi wajah 🧐.
* `main_with_autotrain.py`: Skrip utama untuk menjalankan pengenalan wajah real-time dengan fitur auto-retrain ▶️.
* `test_cv2_face.py`: Skrip sederhana untuk memeriksa versi OpenCV dan pembuatan *recognizer* 🧪.
* `train_model.py`: Skrip untuk melatih model pengenalan wajah dari gambar-gambar di folder `dataset` 🚂.
* `trained_model.yml`: File model pengenalan wajah yang telah dilatih (akan dibuat setelah pelatihan pertama atau sudah ada) 🧠.

## 🛠️ Cara Penggunaan

### ⚙️ Prasyarat

* **🐍 Python 3:** Pastikan Anda telah menginstal Python 3 di sistem Anda.
* **🖼️ OpenCV:** Instal library OpenCV dan *contrib* modules. Anda dapat menginstalnya menggunakan pip:
    ```bash
    pip install opencv-python opencv-contrib-python
    ```
* **🔢 NumPy:** Library NumPy juga diperlukan untuk operasi array:
    ```bash
    pip install numpy
    ```

### 🚦 Langkah-langkah

1.  **⬇️ Klon repositori ini** (jika Anda mengunggahnya ke GitHub).
2.  **📁 Pastikan file `haarcascade_frontalface_default.xml` tersedia** di direktori yang sama dengan skrip Python. Jika belum ada, Anda dapat mengunduhnya dari repositori OpenCV (biasanya terletak di `data/haarcascades/`).
3.  **🚀 Jalankan skrip utama `main_with_autotrain.py`:**
    ```bash
    python main_with_autotrain.py
    ```
4.  **👨‍💻 Penggunaan Aplikasi:**
    * Aplikasi akan membuka jendela yang menampilkan *feed* video dari kamera Anda 📹.
    * Wajah yang terdeteksi akan diberi kotak hijau ✅.
    * Jika wajah dikenali, nama pengguna (berdasarkan label di folder `dataset`) dan tingkat kepercayaan akan ditampilkan 🏷️.
    * Jika wajah tidak dikenali, label "Unknown" 🤔 akan ditampilkan. Wajah yang tidak dikenal akan disimpan secara otomatis ke folder `dataset` 💾 dan model akan dilatih ulang 🔄.
    * Tekan tombol **ESC** untuk keluar dari aplikasi 🚪.

### 🚂 Melatih Model Awal (Jika Diperlukan)

Jika folder `dataset` sudah berisi gambar-gambar wajah yang ingin Anda kenali sejak awal, Anda dapat menjalankan skrip `train_model.py` terlebih dahulu untuk melatih model sebelum menjalankan `main_with_autotrain.py`:

```bash
python train_model.py

