class ArrayKu:
    def _init_(self):
        self.data = []

    def tambah(self, nilai):
        self.data.append(nilai)
        print(f"✔ {nilai} ditambahkan ke array.")

    def update(self, index, nilai):
        if 0 <= index < len(self.data):
            print(f" Update index {index}: {self.data[index]} → {nilai}")
            self.data[index] = nilai
        else:
            print(" Index di luar batas!")

    def hapus(self, index):
        if 0 <= index < len(self.data):
            print(f" Menghapus nilai {self.data[index]} pada index {index}")
            del self.data[index]
        else:
            print(" Index tidak valid!")

    def cari(self, nilai):
        if nilai in self.data:
            posisi = self.data.index(nilai)
            print(f" {nilai} ditemukan pada index {posisi}")
        else:
            print(f" {nilai} tidak ditemukan!")

    def tampil(self):
        print(" Isi array:", self.data)
        print("-" * 40)


# Contoh penggunaan

arr = ArrayKu()

arr.tambah(10)
arr.tambah(20)
arr.tambah(30)
arr.tampil()

arr.update(1, 99)
arr.tampil()

arr.cari(30)
arr.cari(50)

arr.hapus(0)
arr.tampil()