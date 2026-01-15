# OS Simulation Tool - Kelompok 4

Aplikasi berbasis terminal (CLI) ini dibuat untuk mensimulasikan dua konsep inti Sistem Operasi: **CPU Scheduling** dan **Memory Management**. Proyek ini dikembangkan sebagai Tugas Praktikum Minggu 15.

## Fitur Utama

### 1. Simulasi Task Manager (CPU Scheduling)
* **Algoritma:** *First-Come First-Served* (FCFS).
* **Analogi:** Antrean eksekusi aplikasi komputer. Aplikasi yang pertama kali dibuka (datang) akan diproses CPU hingga selesai (*non-preemptive*) sebelum memproses aplikasi berikutnya.
* **Output:** Tabel waktu eksekusi, waktu tunggu (*waiting time*), dan rata-rata *Turnaround Time*.

### 2. Simulasi Multitasking RAM (Memory Management)
* **Algoritma:** *Least Recently Used* (LRU).
* **Analogi:** Manajemen memori saat multitasking. Jika kapasitas RAM penuh dan pengguna membuka aplikasi baru, sistem akan menutup/mengganti aplikasi yang **paling lama tidak digunakan** (*Least Recently Used*) untuk memberi ruang.
* **Output:** Visualisasi isi Frame RAM, status *Hit/Miss*, dan perhitungan *Hit Ratio*.

---

## Struktur Folder

```text
├── code/
│   ├── data/
│   │   ├── cpu_data.csv
│   │   └── mem_data.txt
│   ├── cpu.py 
│   ├── memory.py
│   ├── main.py 
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
├── screenshots/
│   ├── menu_utama.png
│   ├── hasil_cpu.png
│   ├── hasil_memory.png
│   └── demo_docker.png
└── laporan.md

```

---

## Cara Menjalankan

Anda dapat menjalankan aplikasi ini menggunakan dua cara: via Docker (disarankan) atau secara Manual (Python Lokal).

### Cara 1: Menggunakan Docker (Disarankan)

Pastikan Docker Desktop sudah berjalan. Cara ini menjamin aplikasi berjalan tanpa error dependensi.

1. **Build Image**
Buka terminal di dalam folder `code/`, lalu jalankan:
```bash
docker build -t os-sim-kelompok .

```


2. **Jalankan Container**
Gunakan flag `-it` agar bisa berinteraksi dengan menu aplikasi:
```bash
docker run -it --rm os-sim-kelompok

```



### Cara 2: Menjalankan Secara Manual (Local Host)

Pastikan Python 3.14 sudah terinstal di komputer Anda.

1. **Install Dependensi**
```bash
pip install -r requirements.txt

```


2. **Jalankan Aplikasi**
```bash
python main.py

```



---

## Konfigurasi Dataset

Anda dapat mengubah skenario simulasi dengan mengedit file di folder `data/`.

### 1. `data/cpu_data.csv` (Untuk CPU Scheduling)

* **Format:** `NamaProses,WaktuDatang,LamaProses`
* **Contoh Isi:**
```csv
System,0,5
Chrome,1,10
Word,3,2
Spotify,5,4

```



### 2. `data/mem_data.txt` (Untuk Memory LRU)

* **Format:** Nama aplikasi dipisahkan oleh **spasi**.
* **Contoh Isi:**
```text
Chrome Spotify Word Chrome Excel Spotify Word Chrome

```



---

*Dibuat oleh Kelompok [NAMA KELOMPOK] - Praktikum Sistem Operasi 2026*

```

```