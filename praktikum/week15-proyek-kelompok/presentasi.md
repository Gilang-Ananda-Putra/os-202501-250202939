# PRESENTASI PROYEK KELOMPOK: MINI SIMULASI OS

**Topik:** CPU Scheduling (FCFS) & Memory Management (LRU)

**Minggu:** 15

---

## Nama Anggota Kelompok

1. **Gilang Ananda Putra** - [250202939] (Project Lead)
2. **Pasya Awan Rizky Saputro** - [525020259] (Dev CPU)
3. **Faizal Muzaki** - [250202937] (Dev Memory)
4. **Yusuf Anwar** - [250202971] (DevOps & Docs)

---

## 1. PENDAHULUAN

### Latar Belakang
* Mekanisme sistem operasi bekerja di belakang layar (*background*) sehingga sulit dipahami secara visual.
* Kami mengembangkan **OS Simulation Tool** berbasis CLI untuk memvisualisasikan bagaimana CPU memproses antrian dan bagaimana RAM mengatur aplikasi yang berjalan.

### Studi Kasus
1. **Simulasi Task Manager (CPU)**
* Menggunakan algoritma **FCFS (*First-Come First-Served*)**.
* **Analogi:** Seperti antrian printer atau kasir. Aplikasi yang pertama kali dibuka (misal: *System Boot*) akan diselesaikan sepenuhnya oleh CPU sebelum aplikasi berikutnya (*Chrome, Word*) diproses.

2. **Simulasi Multitasking RAM (Memory)**
* Menggunakan algoritma **LRU (*Least Recently Used*)**.
* **Analogi:** Pengguna membuka banyak aplikasi di HP. Saat RAM penuh, sistem tidak membuang aplikasi yang paling tua (FIFO), melainkan membuang aplikasi yang **paling lama tidak disentuh/digunakan** oleh user.

---

## 2. ARSITEKTUR APLIKASI

### Tech Stack
* **Bahasa:** Python 3.14 (Slim Image).
* **Container:** Docker (Menjamin aplikasi jalan di laptop manapun).
* **Library:** `tabulate` (Untuk visualisasi tabel ASCII).

### Desain Modular (*Flat Structure*)

Kami menerapkan struktur folder sederhana namun terorganisir:

1. **Controller (`main.py`):**
* Pusat kendali aplikasi.
* Menangani fitur **Auto-Path Detection** (menggunakan `os.path`) untuk mencegah error "File Not Found" saat membaca dataset.


2. **Logic Modules (`cpu.py` & `memory.py`):**
* `cpu.py`: Menangani logika antrian, sorting arrival time, dan perhitungan waiting time.
* `memory.py`: Menangani simulasi stack memori, pengecekan *Hit/Miss*, dan logika penggantian halaman (replacement).


3. **Dataset (`data/`):**
* Pemisahan data (`.csv` dan `.txt`) dari kode program agar simulasi mudah diubah tanpa coding ulang.



---

## 3. LIVE DEMO

**Skenario Demo via Docker:**

1. **Build & Run:**
```bash
docker build -t os-sim-kelompok .
docker run -it --rm os-sim-kelompok

```


2. **Simulasi 1: CPU Scheduling**
* Input: `cpu_data.csv` (System, Chrome, Word, Spotify).
* Amati: Bagaimana *Waiting Time* dihitung berdasarkan urutan datang.


3. **Simulasi 2: Memory Management**
* Input: `mem_data.txt` (Request acak aplikasi).
* Set Kapasitas RAM: **3 Frame**.
* Amati: Bagaimana sistem membuang aplikasi saat frame penuh.



---

## 4. HASIL & ANALISIS: CPU (FCFS)

**Data Uji:**
* System (Datang: 0, Durasi: 5)
* Chrome (Datang: 1, Durasi: 10)
* Word (Datang: 3, Durasi: 2)
* Spotify (Datang: 5, Durasi: 4)

**Hasil:**
* **Rata-rata Turnaround Time:** 12.25 ms
* **Rata-rata Waiting Time:** 7.00 ms

**Analisis:**
* **Keadilan Antrian:** Proses "System" dieksekusi instan (Waiting Time 0).
* **Convoy Effect:** Proses "Spotify" (hanya 4ms) terpaksa menunggu 12ms karena harus menunggu "Chrome" (10ms) selesai. Ini membuktikan kelemahan FCFS: proses cepat bisa terhambat oleh proses lambat yang datang duluan.

---

## 5. HASIL & ANALISIS: MEMORY (LRU)

**Data Uji:**
* Total Request: 20 Aplikasi berulang (Chrome, Spotify, Word, Excel, dll).
* Kapasitas RAM: 3 Frame.

**Hasil:**
* **Total Page Faults:** 12 kali.
* **Hit Ratio:** 40.00%.

**Analisis:**
* **Perbedaan dengan FIFO:** LRU lebih cerdas. Contoh: Jika "Chrome" masuk frame paling awal tapi sering diakses (status *HIT*), posisinya akan diperbarui menjadi "paling baru".
* **Isu Kapasitas:** Hit Ratio 40% menandakan kapasitas 3 Frame belum cukup ideal untuk menangani variasi aplikasi yang dibuka, menyebabkan *Thrashing* (terlalu sering gonta-ganti isi memori).

---

## 6. TIM & KONTRIBUSI

Proyek dikerjakan secara kolaboratif menggunakan Git Branching:

| Nama Anggota | Peran | Kontribusi Detail |
| --- | --- | --- |
| **Gilang Ananda Putra** | Project Lead & Integrator | - Mengembangkan `main.py` (sistem menu)<br> - Membuat `Dockerfile` agar aplikasi berjalan di container <br> - Menginisialisasi Git Repo, melakukan *Merge Request* dari seluruh anggota<br> - Pengujian Aplikasi<br> - Finalisasi kode. |
| **Pasya Awan Rizky Saputro** | - Developer Modul CPU | - Mengimplementasikan logika FCFS di `cpu.py`<br> - Membuat dataset CSV studi kasus<br> - Mendesain format tabel output CPU. |
| **Faizal Muzaki** | - Developer Modul Memory | Mengimplementasikan logika LRU di `memory.py`<br> - Menangani parsing input file TXT<br> - Logika penggantian halaman (*replacement*). |
| **Yusuf Anwar** | Docs & QA | - Melakukan pengujian (*debugging* path file)<br> - Mengambil *screenshot*<br> - Menyusun laporan. |

---

## 7. TANTANGAN & SOLUSI

1. **Masalah Path File:**
* *Issue:* Python gagal menemukan file data saat dijalankan dari folder luar.
* *Solusi:* Menggunakan `os.path.abspath(__file__)` untuk mendeteksi lokasi skrip secara otomatis.


2. **Environment:**
* *Issue:* Library `tabulate` tidak ada di komputer dosen/teman.
* *Solusi:* Menggunakan Docker untuk membungkus semua dependensi jadi satu paket.



---

**TERIMA KASIH**

*Ada Pertanyaan?*

