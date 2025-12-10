# Program Demonstrasi Array Satu Dimensi
#Hasil modifikasi

# 1. Deklarasi array satu dimensi
angka = [10, 15, 20, 25, 30]

print(" ARRAY AWAL ")
print("Isi array:", angka)
print()

# 2. Menampilkan elemen satu per satu
print(" MENAMPILKAN ELEMEN ARRAY ")
for i in range(len(angka)):
    print(f"Indeks {i} -> {angka[i]}")
print()

# 3. Menambah elemen baru ke array
print(" MENAMBAHKAN DATA BARU ")
angka.append(35)
angka.append(40)
print("Array setelah ditambah:", angka)
print()

# 4. Menghapus elemen dari array
print(" MENGHAPUS DATA ")
angka.remove(20)  # hapus nilai 20
print("Array setelah menghapus nilai 20:", angka)
print()

# 5. Mengubah nilai dalam array
print(" MENGUBAH DATA ")
angka[2] = 90   # ubah indeks ke-2
print("Array setelah perubahan:", angka)
print()

# 6. Mencari elemen dalam array
print(" MENCARI DATA ")
cari = 40
if cari in angka:
    print(f"Angka {cari} ditemukan pada indeks:", angka.index(cari))
else:
    print(f"Angka {cari} tidak ditemukan.")
print()

# 7. Menghitung jumlah elemen dalam array
print(" JUMLAH ELEMEN ARRAY ")
print("Total elemen:", len(angka))
print()

# 8. Mencari nilai maksimum dan minimum
print(" NILAI MAKSIMUM & MINIMUM ")
print("Nilai maksimum:", max(angka))
print("Nilai minimum:", min(angka))
print()

# 9. Mengurutkan array
print(" MENGURUTKAN ARRAY ")
angka.sort()
print("Array setelah diurutkan:", angka)
print()

# 10. Input array dari pengguna
print(" INPUT ARRAY DARI PENGGUNA ")
user_array = []

jumlah_data = int(input("Masukkan berapa banyak data yang ingin dimasukkan: "))

for i in range(jumlah_data):
    nilai = int(input(f"Masukkan nilai ke-{i+1}: "))
    user_array.append(nilai)

print("Array yang dimasukkan pengguna:", user_array)
print()

# 11. Hitung rata-rata dari array
print(" MENGHITUNG RATA-RATA ")
if len(user_array) > 0:
    rata = sum(user_array) / len(user_array)
    print("Rata-rata nilai:", rata)
else:
    print("Tidak ada data untuk dihitung.")
print("\n PROGRAM SELESAI ")