# Fractal-Based Plant Disease Analysis Suite

> **Proyek Capstone 5**: Sistem Deteksi dan Diagnosis Penyakit Daun Tanaman Berbasis Fitur Dimensi Fraktal dan Lakunaritas  
> **Program Studi**: S1 Ilmu Komputer / Informatika, FMIPA, Universitas Gadjah Mada  
> **Anggota Tim Pengembang**:  
> - Aji Kusuma Putra (NIM: 22/503701/PA/21657)  
> - Rayhan Haldi Hermawan (NIM: 24/545406/PA/23176)  

---

## Ringkasan Proyek
Menganalisis tekstur daun dan iregularitas kontur lesi nekrotik menggunakan dimensi fraktal (*Box-Counting Fractal Dimension*) dan lakunaritas permukaan untuk mendiagnosis penyakit tanaman (sehat, bercak bakteri, karat daun).

### Pembagian Tugas Tim 4 Mahasiswa
1. **Mahasiswa 1**: Segmentasi Daun & Isolasi Lesi Berbasis Ruang Warna.
2. **Mahasiswa 2**: Ekstraksi Vektor Fitur Dimensi Fraktal & Lakunaritas.
3. **Mahasiswa 3**: Pembangunan Model Klasifikasi & Validasi Diagnostik.
4. **Mahasiswa 4**: Antarmuka Grafis (Tkinter GUI), Visualisasi Fitur, & Evaluasi Metrik Klasifikasi.

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
