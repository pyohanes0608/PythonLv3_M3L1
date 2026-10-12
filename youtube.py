
import sqlite3

# 1. Membuat koneksi ke database
conn = sqlite3.connect("youtube_favorit.db")
cursor = conn.cursor()

# 2. Membuat tabel
cursor.execute("""
CREATE TABLE IF NOT EXISTS video_youtube (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    judul TEXT NOT NULL,
    tautan TEXT NOT NULL,
    kreator TEXT,
    tanggal_rilis TEXT,
    deskripsi TEXT
)
""")

conn.commit()
print("Tabel berhasil dibuat!")

# 3. Menambahkan beberapa video favorit
cursor.execute("""
INSERT INTO video_youtube
(judul, tautan, kreator, tanggal_rilis, deskripsi)
VALUES (?, ?, ?, ?, ?)
""", (
    "Belajar Python untuk Pemula",
    "https://www.youtube.com/watch?v=contoh1",
    "Kreator Python",
    "2026-01-10",
    "Tutorial dasar pemrograman Python."
))

cursor.execute("""
INSERT INTO video_youtube
(judul, tautan, kreator, tanggal_rilis, deskripsi)
VALUES (?, ?, ?, ?, ?)
""", (
    "Belajar SQLite",
    "https://www.youtube.com/watch?v=contoh2",
    "Kreator Database",
    "2026-02-15",
    "Belajar database menggunakan SQLite."
))

conn.commit()
print("Video berhasil ditambahkan!")

# 4. Menampilkan semua data dari tabel
print("\n=== DAFTAR VIDEO FAVORIT ===")

cursor.execute("SELECT * FROM video_youtube")
data = cursor.fetchall()

for video in data:
    print(video)

# 5. Mengubah satu entri menggunakan UPDATE
cursor.execute("""
UPDATE video_youtube
SET judul = ?, deskripsi = ?
WHERE id = ?
""", (
    "Belajar Python Lengkap",
    "Tutorial Python dari dasar hingga mahir.",
    1
))

conn.commit()
print("\nVideo dengan ID 1 berhasil diperbarui!")

# Menampilkan data setelah UPDATE
print("\n=== DATA SETELAH UPDATE ===")

cursor.execute("SELECT * FROM video_youtube")
for video in cursor.fetchall():
    print(video)

# 6. Menghapus satu rekaman menggunakan DELETE
cursor.execute("""
DELETE FROM video_youtube
WHERE id = ?
""", (2,))

conn.commit()
print("\nVideo dengan ID 2 berhasil dihapus!")

# Menampilkan data setelah DELETE
print("\n=== DATA SETELAH DELETE ===")

cursor.execute("SELECT * FROM video_youtube")
for video in cursor.fetchall():
    print(video)

# 7. Menutup koneksi database
conn.close()
print("\nKoneksi database ditutup.")
