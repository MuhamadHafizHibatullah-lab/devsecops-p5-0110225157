# TaskFlow — DevSecOps Pipeline

## 1. Deskripsi Aplikasi

TaskFlow adalah aplikasi berbasis Python untuk mengelola daftar tugas. Pengguna dapat menambahkan tugas, melihat daftar tugas, dan menandai tugas sebagai selesai.

## 2. Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Unit testing: unittest
- SAST: Bandit
- CI/CD: GitHub Actions
- Quality Gate: Bandit dengan batas severity dan confidence

## 3. Cara Menjalankan Aplikasi

Pastikan Python telah terpasang.

```bash
python -m venv .venv
```

Aktifkan virtual environment sesuai sistem operasi, lalu jalankan:

```bash
pip install -r requirements.txt
python main.py
```

Untuk menjalankan unit test:

```bash
python -m unittest discover -s tests -v
```

## 4. Overview Pipeline DevSecOps

Pipeline menggunakan GitHub Actions dan berjalan ketika ada push ke branch `main` atau pull request menuju branch `main`.

Pipeline terdiri dari dua job:

1. **build** — memasang dependensi dan menjalankan unit test.
2. **sast-scan** — menjalankan Bandit untuk menganalisis potensi kerentanan keamanan pada source code.

Job `sast-scan` hanya berjalan setelah job `build` berhasil. Quality Gate membuat job SAST gagal apabila Bandit menemukan temuan dengan severity dan confidence sesuai ambang yang ditentukan.

## 5. Tujuan

Pipeline ini menerapkan prinsip Shift Left Security dengan memasukkan pemeriksaan keamanan sejak tahap pengembangan dan sebelum perubahan kode diterima.
