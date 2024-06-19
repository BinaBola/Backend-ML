# Instalasi dan Penggunaan Aplikasi Flask

Aplikasi ini menggunakan Flask sebagai framework web untuk membuat API prediksi gambar menggunakan model TensorFlow. Aplikasi ini memerlukan beberapa dependensi yang harus diinstal sebelum dapat dijalankan.

## Prasyarat

Pastikan Anda sudah menginstal:

Python 3.9 atau versi yang lebih baru
pip (package installer untuk Python)
Virtual environment (opsional tetapi direkomendasikan)

## Langkah-langkah Instalasi

1. Clone Repository
Clone repository dari GitHub ke komputer Anda.

```bash
git clone =https://github.com/BinaBola/Backend-ML.git
cd Backend-ML
```

2. Buat dan Aktifkan Virtual Environment

```
python -m venv .venv
```

- Windows:

```
.venv\Scripts\activate
```

- Linux & MacOS:

```
source .venv/bin/activate
```

3. Instal Dependensi

```
pip install -r requirements.txt
```
4. Pastikan Model dan Data Tersedia
Pastikan file model (model.h5) tersedia di direktori root proyek.

5. Jalankan Aplikasi
Jalankan aplikasi Flask menggunakan perintah berikut:

```bash
python local.py
```

Buka browser anda dan pergi ke http://127.0.0.1:8080 untuk memeriksa API.

## Endpoint API

Predict
Endpoint ini digunakan untuk mengunggah gambar dan mendapatkan prediksi.

URL: /predict
Method: POST
Content-Type: multipart/form-data
Form Data:
image: File gambar (jpg, jpeg, png)

## Penggunaan

Gunakan titik akhir /predict untuk membuat prediksi berdasarkan gambar input.

```
curl -X POST -F "image=@path/to/your/image.jpg" http://127.0.0.1:8080/predict
```

Ganti path/to/your/image.jpg dengan path ke file gambar yang ingin Anda prediksi.

## Contoh Response

```
{
    "Message": "Model predicted successfully",
    "Food Prediction": "apel",
    "Calories": 52,
    "Carbs": 13.81,
    "Protein": 0.26,
    "Fat": 0.17,
    "Confidence": 0.95
}
```
