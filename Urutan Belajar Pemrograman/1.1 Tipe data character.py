# Program Demonstrasi Tipe Data Character

# 1. Deklarasi Character
karakter1 = 'W'
karakter2 = 'b'
karakter3 = '4'
karakter4 = '?'

print(" Contoh Tipe Data Character ")
print("Karakter 1:", karakter1)
print("Karakter 2:", karakter2)
print("Karakter 3:", karakter3)
print("Karakter 4:", karakter4)
print()

# 2. Meminta Input Karakter dari Pengguna
print(" Input Character dari Pengguna ")
karakter_user = input("Masukkan 1 karakter: ")

# Pastikan hanya 1 karakter
if len(karakter_user) != 1:
    print("Error: Harus memasukkan tepat 1 karakter!")
else:
    print("Karakter yang dimasukkan:", karakter_user)
    print()

    # 3. Mengecek jenis karakter
    print(" Pengecekan Karakter ")
    if karakter_user.isalpha():
        print("Karakter ini adalah huruf.")
    elif karakter_user.isdigit():
        print("Karakter ini adalah angka.")
    else:
        print("Karakter ini adalah simbol atau karakter khusus.")

    print()

    # 4. Mengecek huruf besar atau kecil
    if karakter_user.isalpha():
        if karakter_user.isupper():
            print("Huruf tersebut adalah huruf BESAR.")
        else:
            print("Huruf tersebut adalah huruf kecil.")
    print()

    # 5. Mengecek vokal atau konsonan
    vokal = "aiueoAIUEO"
    if karakter_user.isalpha():
        if karakter_user in vokal:
            print("Huruf tersebut adalah huruf VOKAL.")
        else:
            print("Huruf tersebut adalah huruf KONSONAN.")

print("\n Program Selesai ")