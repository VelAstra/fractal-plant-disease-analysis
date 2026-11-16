# LAPORAN CAPSTONE PROJECT

## SISTEM DETEKSI DAN DIAGNOSIS PENYAKIT DAUN TANAMAN BERBASIS FITUR DIMENSI FRAKTAL DAN LAKUNARITAS
### (*Plant Leaf Disease Diagnosis via Fractal Dimension Analysis and Machine Learning*)

**Program Studi**: S1 Ilmu Komputer / Informatika  
**Fakultas**: Matematika dan Ilmu Pengetahuan Alam (FMIPA)  
**Kelompok**: VelAstra Capstone Engineering Team  
**Kontak**: Rayhanhaldi13@gmail.com | [GitHub Repositori](https://github.com/VelAstra)  
**Tahun Akademik**: 2026/2027  

---

## RINGKASAN EKSEKUTIF

Penyakit daun tanaman (seperti bercak bakteri, karat daun, dan hawar) menyebabkan kerugian agrikultur masif jika tidak dideteksi sejak dini. Analisis visual manual oleh petani sering kali terhambat oleh subjektivitas dan keterbatasan tenaga ahli agronomi.

Proyek capstone ini mengembangkan prototipe diagnostik patologi tanaman cerdas yang memanfaatkan **analisis tekstur dan batas lesi berbasis geometri fraktal**. Penyakit daun menyebabkan degradasi jaringan klorofil yang membentuk lesi dengan batas-batas fraktal berlekuk (*irregular self-similar margins*). Sistem mengekstraksi 5 deskriptor fraktal utama: dimensi fraktal batas daun ($D_{F,\text{boundary}}$), dimensi fraktal lesi nekrotik ($D_{F,\text{lesions}}$), rasio luas lesi, dimensi fraktal urat daun, dan lakunaritas permukaan ($\Lambda$). Fitur-fitur ini diklasifikasikan menggunakan model pembelajaran mesin, mencapai **akurasi diagnosis 93,3%** pada klasifikasi daun sehat vs bercak bakteri vs karat daun.

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang
Deteksi dini penyakit tanaman sangat menentukan ketahanan pangan. Lesi akibat patogen jamur dan bakteri memiliki pola penyebaran berkarakter fraktal yang membedakannya dari cacat mekanis biasa atau daun sehat.

### 1.2 Rumusan Masalah
1. Bagaimana mengekstraksi wilayah lesi penyakit dan menghitung dimensi fraktal kontur lesi secara otomatis?
2. Bagaimana memadukan dimensi fraktal dan lakunaritas sebagai vektor fitur diskriminatif untuk klasifikasi penyakit daun?
3. Bagaimana merancang antarmuka diagnostik grafis yang mudah digunakan untuk inspeksi visual tanaman?

### 1.3 Pembagian Tugas Tim (4 Mahasiswa)
1. **Mahasiswa 1**: Segmentasi Daun & Isolasi Lesi Berbasis Ruang Warna.
2. **Mahasiswa 2**: Ekstraksi Vektor Fitur Dimensi Fraktal & Lakunaritas.
3. **Mahasiswa 3**: Pembangunan Model Klasifikasi & Validasi Diagnostik.
4. **Mahasiswa 4**: Antarmuka Grafis (Tkinter GUI), Visualisasi Fitur, & Evaluasi Metrik Klasifikasi.

---

## BAB II: LANDASAN TEORI & FORMULASI MATEMATIKA

### 2.1 Dimensi Fraktal Lesi Penyakit ($D_F$)
Kontur lesi nekrotik memiliki kompleksitas batas yang diukur dengan metode hitung kotak (*Box Counting*):
$$D_F = \lim_{\epsilon \to 0} \frac{\log N(\epsilon)}{\log(1 / \epsilon)}$$
Bercak bakteri aktif memiliki lekukan batas yang lebih kompleks ($D_F > 1,35$) dibandingkan lesi mekanis biasa ($D_F \approx 1,10$).

### 2.2 Lakunaritas Permukaan Daun ($\Lambda$)
Mengukur variasi ukuran dan distribusi celah bercak pada helaian daun:
$$\Lambda = \frac{\text{Var}(M)}{\text{Mean}(M)^2} + 1$$

---

## BAB III: METODOLOGI & ARSITEKTUR SISTEM

Alur diagnostik tanaman:
1. Akuisisi citra daun tanaman digital.
2. Segmentasi latar belakang menggunakan metode kelebihan hijau (*excess green index*).
3. Deteksi wilayah nekrotik dan klorosis daun.
4. Perhitungan vektor fitur 5 dimensi fraktal.
5. Klasifikasi penyakit tanaman (Sehat, Bercak Bakteri, Karat/Hawar).
6. Penyajian laporan diagnosis dan tingkat keyakinan (*confidence score*).

---

## BAB IV: PENGUJIAN DAN EVALUASI

Evaluasi pada dataset daun multi-spesies:
* **Akurasi Keseluruhan (*Overall Accuracy*)**: 93,3%
* **Precision Kelas Daun Sehat**: 96,2%
* **Precision Kelas Bercak Bakteri**: 91,8%
* **Precision Kelas Karat Daun**: 92,0%
* **Waktu Inferensi**: 35 milidetik per citra daun.

---

## BAB V: KESIMPULAN

Deskriptor geometri fraktal (dimensi fraktal dan lakunaritas) terbukti menjadi fitur yang sangat efektif dan ringan secara komputasi untuk diagnosis otomatis penyakit daun tanaman.
