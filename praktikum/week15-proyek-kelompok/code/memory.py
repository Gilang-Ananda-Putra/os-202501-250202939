import os
from tabulate import tabulate

def solve_lru(file_path, capacity=3):
    print(f"\n[INFO] Menjalankan Memory Management (LRU)...")
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' tidak ditemukan!")
        return

    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            # Ganti koma jadi spasi dulu, baru split (jaga-jaga formatnya beda)
            pages = content.replace(',', ' ').split()
    except Exception as e:
        print(f"Error membaca file: {e}")
        return

    if not pages:
        print("Error: File kosong!")
        return

    frames = []
    page_faults = 0
    history = []

    for page in pages:
        status = ""
        if page not in frames:
            status = "MISS"
            page_faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0) 
                frames.append(page)
        else:
            status = "HIT"
            frames.remove(page)
            frames.append(page) 
        
        history.append([page, str(frames), status])

    hit_ratio = ((len(pages) - page_faults) / len(pages)) * 100
    
    print(tabulate(history, headers=["App Request", "RAM Frames", "Status"], tablefmt="simple"))
    print(f"\n> Total Requests : {len(pages)}")
    print(f"> Total Page Faults: {page_faults}")
    print(f"> Hit Ratio        : {hit_ratio:.2f}%")
