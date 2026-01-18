import json
import os

def calculate_need(need, max_res, alloc, n_proc, n_res):
    # Menghitung matriks Need = Max - Allocation
    for i in range(n_proc):
        for j in range(n_res):
            need[i][j] = max_res[i][j] - alloc[i][j]

def is_safe(processes, avail, max_res, alloc, n_proc, n_res):
    need = [[0] * n_res for _ in range(n_proc)]
    calculate_need(need, max_res, alloc, n_proc, n_res)

    finish = [False] * n_proc
    safe_seq = [0] * n_proc
    work = [0] * n_res

    for i in range(n_res):
        work[i] = avail[i]

    print(f"\n--- Membaca Dataset dari File Eksternal ---")
    print("\n--- Status Awal Sistem ---")
    print("P\tAlloc\tMax\tNeed")
    for i in range(n_proc):
        print(f"P{i}\t{alloc[i]}\t{max_res[i]}\t{need[i]}")
    print(f"Available: {work}\n")

    count = 0
    print("--- Proses Eksekusi ---")
    while count < n_proc:
        found = False
        for p in range(n_proc):
            if not finish[p]:
                if all(need[p][j] <= work[j] for j in range(n_res)):
                    print(f"[OK] P{p} dieksekusi. Need {need[p]} <= Avail {work}")
                    for k in range(n_res):
                        work[k] += alloc[p][k]
                    safe_seq[count] = p
                    finish[p] = True
                    found = True
                    count += 1
                    print(f"     P{p} selesai. Resource dilepas. Avail sekarang: {work}")
        
        if not found:
            print("\n[!] Sistem tidak aman (Unsafe State) - Terdeteksi potensi Deadlock!")
            return False

    print("\n--- Hasil Akhir ---")
    print("[Success] Sistem dalam SAFE STATE.")
    print("Urutan Aman (Safe Sequence):", end=" ")
    print(" -> ".join(f"P{p}" for p in safe_seq))
    return True

def load_data(filename):
    # Cek lokasi file agar aman saat dijalankan dari folder manapun
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan di {base_path}")
        return None

if __name__ == "__main__":
    # Load dataset dari file JSON
    data = load_data('dataset.json')

    if data:
        processes = list(range(data['n_proc']))
        
        # Jalankan fungsi utama dengan data dari JSON
        is_safe(
            processes, 
            data['available'], 
            data['max_res'], 
            data['allocation'], 
            data['n_proc'], 
            data['n_res']
        )