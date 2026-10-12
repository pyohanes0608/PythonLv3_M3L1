import sqlite3

# =====================================================================
# 1. KONEKSI & PEMBUATAN TABEL (CREATE)
# =====================================================================
# Membuat koneksi ke database 'tutorial.db'
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

# Menghapus tabel lama jika ada agar demonstrasi bisa diulang dari awal
cur.execute("DROP TABLE IF EXISTS movie")

# Membikin tabel dengan tipe data dan aturan NOT NULL
cur.execute("""
    CREATE TABLE IF NOT EXISTS movie(
        title TEXT NOT NULL, 
        year INTEGER NOT NULL, 
        score REAL
    )
""")
print("1. Tabel 'movie' berhasil dibuat.")


# =====================================================================
# 2. MEMASUKKAN DATA (INSERT)
# =====================================================================
# A. Memasukkan data tunggal menggunakan execute()
cur.execute("INSERT INTO movie VALUES ('Monty Python and the Holy Grail', 1975, 8.2)")

# B. Memasukkan data dengan menentukan kolom tertentu & menggunakan placeholder (?)
cur.execute("INSERT INTO movie (title, year) VALUES (?, ?)", ('The Imitation Game', 2014))

# C. Memasukkan banyak data sekaligus menggunakan executemany()
data_banyak = [
    ("And Now for Something Completely Different", 1971, 7.5),
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data_banyak)

# Wajib melakukan commit agar data tersimpan permanen
con.commit()
print("2. Semua data contoh berhasil dimasukkan.")


# =====================================================================
# 3. MEMBACA DATA (SELECT)
# =====================================================================
print("\n3. MENAMPILKAN DATA (SELECT):")

# A. Mengambil semua data (SELECT *)
print("\n--- Semua Film di Database ---")
for row in cur.execute("SELECT * FROM movie"):
    print(row)

# B. Mengambil data dengan filter kondisi (WHERE) dan pengurutan (ORDER BY)
print("\n--- Film tahun di atas 1975 (Diurutkan berdasarkan Tahun) ---")
query_filter = """
    SELECT year, title 
    FROM movie 
    WHERE year > 1975 
    ORDER BY year
"""
for row in cur.execute(query_filter):
    print(f"Tahun: {row[0]} | Judul: {row[1]}")


# =====================================================================
# 4. MEMPERBARUI DATA (UPDATE)
# =====================================================================
# Mengubah score menjadi 10 untuk film tertentu
cur.execute("""
    UPDATE movie 
    SET score = 10 
    WHERE title = 'Monty Python and the Holy Grail'
""")
con.commit()

print("\n4. DATA SETELAH DI-UPDATE:")
# Cek apakah datanya sudah berubah
for row in cur.execute("SELECT title, score FROM movie WHERE title = 'Monty Python and the Holy Grail'"):
    print(f"Hasil Update -> Film: {row[0]} | Skor Baru: {row[1]}")


# =====================================================================
# 5. MENGHAPUS DATA BARIS (DELETE)
# =====================================================================
# Menghapus film yang memiliki skor kurang dari 8
cur.execute("DELETE FROM movie WHERE score < 8")
con.commit()

print("\n5. DATA SETELAH DI-DELETE (Skor < 8 Dihapus):")
# 'The Imitation Game' juga ikut terhapus karena skornya NULL (dianggap < 8 dalam operasi ini)
for row in cur.execute("SELECT title, score FROM movie"):
    print(row)


# =====================================================================
# 6. MENGHAPUS TABEL (DROP) & MENUTUP KONEKSI
# =====================================================================
# Menghapus seluruh struktur tabel beserta isinya dari database
cur.execute("DROP TABLE movie")
con.commit()
print("\n6. Tabel 'movie' telah dihapus (DROP TABLE).")

# Menutup koneksi database
con.close()
print("Koneksi database ditutup. Selesai!")
