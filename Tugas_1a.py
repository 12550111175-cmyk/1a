# ==============================================================================
# TUGAS MANDIRI 1A - STRUKTUR DATA DAN ANALISIS KOMPLEKSITAS
# ==============================================================================

from collections import deque

print("=== DEMO IMPLEMENTASI STRUKTUR DATA KASUS SISTEM AKADEMIK ===\n")

# ------------------------------------------------------------------------------
# 1. ARRAY / LIST (Penyimpanan Data Secara Berurutan)
# Akses berbasis indeks berjalan dengan kompleksitas O(1)
# ------------------------------------------------------------------------------
print("1. Array / List (Penyimpanan Data Berurutan)")
daftar_mahasiswa = [
    "Mahasiswa_01", "Mahasiswa_02", "Mahasiswa_03", "Mahasiswa_04", "Mahasiswa_05",
    "Mahasiswa_06", "Mahasiswa_07", "Mahasiswa_08", "Mahasiswa_09", "Mahasiswa_10"
]
print(f"   Daftar 10 Mahasiswa: {daftar_mahasiswa}")
print(f"   Akses Data Indeks Ke-0 (Akses O(1)): {daftar_mahasiswa[0]}\n")


# ------------------------------------------------------------------------------
# 2. STACK (Fitur Undo Riwayat Aksi)
# Menerapkan prinsip LIFO (Last In First Out), operasi push/pop O(1)
# ------------------------------------------------------------------------------
print("2. Stack (Fitur Undo Riwayat Aksi - LIFO)")
stack_undo = []

# Menambahkan 10 riwayat aksi (Push)
for i in range(1, 11):
    stack_undo.append(f"Aksi_{i}: Edit Data Mahasiswa_{i:02d}")

print(f"   Total Aksi Tersimpan: {len(stack_undo)}")
print(f"   Aksi Terakhir: '{stack_undo[-1]}'")

# Membatalkan aksi terakhir (Pop)
aksi_dibatalkan = stack_undo.pop()
print(f"   Melakukan Undo (Pop O(1)): Membatalkan '{aksi_dibatalkan}'")
print(f"   Sisa Aksi Tersimpan: {len(stack_undo)}\n")


# ------------------------------------------------------------------------------
# 3. QUEUE (Sistem Antrean Pengolahan Data)
# Menerapkan prinsip FIFO (First In First Out), operasi enqueue/dequeue O(1)
# ------------------------------------------------------------------------------
print("3. Queue (Sistem Antrean Pengolahan Data - FIFO)")
# Mengisi antrean awal dengan 10 data acak
antrean_pendaftaran = deque([f"Mahasiswa_{i:02d}" for i in range(1, 11)])

print(f"   Jumlah Antrean Awal: {len(antrean_pendaftaran)}")
print(f"   Daftar Antrean: {list(antrean_pendaftaran)}")

# Memproses antrean terdepan (Dequeue)
diproses = antrean_pendaftaran.popleft()
print(f"   Diproses Terlebih Dahulu (Dequeue O(1)): {diproses}")
print(f"   Sisa Antrean: {list(antrean_pendaftaran)}\n")


# ------------------------------------------------------------------------------
# 4. HASH TABLE / DICTIONARY (Pencarian Data Berdasarkan Key / NIM Dummy)
# Menerapkan pemetaan Key-Value, pencarian berkecepatan rata-rata O(1)
# ------------------------------------------------------------------------------
print("4. Hash Table / Dictionary (Pencarian Data Berdasarkan Key NIM Dummy)")

# Dictionary dengan 10 data dummy NIM acak
dict_mahasiswa = {
    "12000000001": {"nama": "Mahasiswa_A", "prodi": "Teknik Informatika"},
    "12000000002": {"nama": "Mahasiswa_B", "prodi": "Sistem Informasi"},
    "12000000003": {"nama": "Mahasiswa_C", "prodi": "Teknik Elektro"},
    "12000000004": {"nama": "Mahasiswa_D", "prodi": "Teknik Informatika"},
    "12000000005": {"nama": "Mahasiswa_E", "prodi": "Sistem Informasi"},
    "12000000006": {"nama": "Mahasiswa_F", "prodi": "Teknik Elektro"},
    "12000000007": {"nama": "Mahasiswa_G", "prodi": "Teknik Informatika"},
    "12000000008": {"nama": "Mahasiswa_H", "prodi": "Sistem Informasi"},
    "12000000009": {"nama": "Mahasiswa_I", "prodi": "Teknik Elektro"},
    "12000000010": {"nama": "Mahasiswa_J", "prodi": "Teknik Informatika"},
}

# Pencarian instan menggunakan Key (NIM Dummy)
nim_cari = "12000000005"
hasil_pencarian = dict_mahasiswa.get(nim_cari)

print(f"   Mencari Key NIM '{nim_cari}' (Pencarian O(1))...")
if hasil_pencarian:
    print(f"   Data Ditemukan -> Nama: {hasil_pencarian['nama']}, Prodi: {hasil_pencarian['prodi']}")
else:
    print("   Data Tidak Ditemukan")