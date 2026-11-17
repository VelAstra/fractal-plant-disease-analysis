# Fractal-Based Plant Disease Analysis Suite

> **Proyek Capstone 5**: Sistem Deteksi dan Diagnosis Penyakit Daun Tanaman Berbasis Fitur Dimensi Fraktal dan Lakunaritas  
> **Program Studi**: S1 Ilmu Komputer / Informatika, FMIPA, Universitas Gadjah Mada  
> **Anggota Tim Pengembang**:  
> - Aji Kusuma Putra (NIM: 22/503701/PA/21657)  
> - Rayhan Haldi Hermawan (NIM: 24/545406/PA/23176)  

---

## Ringkasan Proyek
Menganalisis tekstur daun dan iregularitas kontur lesi nekrotik menggunakan dimensi fraktal (*Box-Counting Fractal Dimension*) dan lakunaritas permukaan untuk mendiagnosis penyakit tanaman (sehat, bercak bakteri, karat daun).

### Pembagian Tugas Tim (2 Mahasiswa)
1. **Aji Kusuma Putra** (`22/503701/PA/21657`): Segmentasi daun dan isolasi lesi bercak daun berbasis ruang warna HSV/Excess Green, serta ekstraksi vektor 5 deskriptor dimensi fraktal kontur dan lakunaritas permukaan. (Modul: `sample_data/generate_leaf_dataset.py`, `core/fractal_features.py`).
2. **Rayhan Haldi Hermawan** (`24/545406/PA/23176`): Pembangunan model classifier machine learning, validasi akurasi diagnostik, Desktop GUI Tkinter, integrasi CLI, visualisasi diagram radar fitur, dan evaluasi metrik (Accuracy, Precision, Recall). (Modul: `core/classifier.py`, `core/evaluation.py`, `gui/app.py`, `cli.py`).

---

## Cara Menjalankan

```bash
# Menjalankan diagnosis pada citra daun sampel
python cli.py diagnose sample_data/leaf_bacterial_spot.png

# Menjalankan antarmuka grafis
python cli.py gui

# Menjalankan uji otomatis
python -m unittest discover tests
```
