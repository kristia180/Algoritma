# Program Demonstrasi Tipe Data Integer

# 1. Deklarasi Integer
angka1 = 20
angka2 = 32
angka3 = -15
angka4 = 250

print(" Contoh Tipe Data Integer ")
print("Angka 1:", angka1)
print("Angka 2:", angka2)
print("Angka 3:", angka3)
print("Angka 4:", angka4)
print()

# 2. Operasi Aritmatika
print(" Operasi Aritmatika pada Integer ")
penjumlahan = angka1 + angka2
pengurangan = angka2 - angka1
perkalian = angka1 * angka3
pembagian = angka4 / angka1  # pembagian integer
modulus = angka2 % angka1      # sisa bagi

print("Penjumlahan:", penjumlahan)
print("Pengurangan:", pengurangan)
print("Perkalian:", perkalian)
print("Pembagian (integer):", pembagian)
print("Modulus (sisa bagi):", modulus)
print()

# 3. Input Integer dari Pengguna
print(" Input Integer dari Pengguna ")
try:
    angka_user = int(input("Masukkan angka bulat: "))
    print("Angka yang dimasukkan:", angka_user)
except:
    print("Error: yang dimasukkan bukan angka bulat!")
    angka_user = None
print()

# 4. Mengecek sifat angka
if angka_user is not None:
    print(" Pengecekan Sifat Integer ")

    # Cek Positif, Negatif, atau Nol
    if angka_user > 0:
        print("Angka tersebut adalah POSITIF.")
    elif angka_user < 0:
        print("Angka tersebut adalah NEGATIF.")
    else:
        print("Angka tersebut adalah NOL.")

    # Cek Ganjil atau Genap
    if angka_user % 2 == 0:
        print("Angka tersebut adalah GENAP.")
    else:
        print("Angka tersebut adalah GANJIL.")

print("\n Program Selesai ")