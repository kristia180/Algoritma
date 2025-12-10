# Program Demonstrasi Tipe Data Floating Point

# 1. Deklarasi Floating Point
float1 = 4.13
float2 = 15.25
float3 = -5.2
float4 = 310.2

print(" Contoh Tipe Data Floating Point ")
print("Float 1:", float1)
print("Float 2:", float2)
print("Float 3:", float3)
print("Float 4:", float4)
print()

# 2. Operasi Aritmatika
print(" Operasi Aritmatika pada Floating Point ")
penjumlahan = float1 + float2
pengurangan = float2 - float3
perkalian = float1 * float3
pembagian = float4 / float1
pangkat = float1 ** 2

print("Penjumlahan:", penjumlahan)
print("Pengurangan:", pengurangan)
print("Perkalian:", perkalian)
print("Pembagian:", pembagian)
print("Pangkat:", pangkat)
print()

# 3. Pembulatan Angka
print(" Pembulatan Floating Point ")
print("Round float1:", round(float1))
print("Round float2:", round(float2))
print("Floor (pembulatan ke bawah):", int(float2))  # cara simpel
print()

# 4. Input Floating Point dari Pengguna
print(" Input Floating Point dari Pengguna ")
try:
    angka_user = float(input("Masukkan angka desimal: "))
    print("Angka yang dimasukkan:", angka_user)
except:
    print("Error: yang dimasukkan bukan angka desimal!")
    angka_user = None
print()

# 5. Pengecekan angka floating point
if angka_user is not None:
    print(" Pengecekan Angka ")

    if angka_user > 0:
        print("Angka tersebut adalah POSITIF.")
    elif angka_user < 0:
        print("Angka tersebut adalah NEGATIF.")
    else:
        print("Angka tersebut adalah NOL.")

    # Cek apakah memiliki nilai pecahan (desimal)
    if angka_user % 1 == 0:
        print("Angka tersebut TIDAK memiliki pecahan (sebenarnya integer).")
    else:
        print("Angka tersebut memiliki pecahan (desimal).")

print("\n Program Selesai ")