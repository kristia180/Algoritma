class VariabelDinamis:
    def _init_(self, nilai_awal=None):
        self.nilai = nilai_awal
        self.tipe = type(nilai_awal)

    def set(self, nilai_baru):
        print(f"✔ Memperbarui nilai: {self.nilai} → {nilai_baru}")
        self.nilai = nilai_baru
        self.tipe = type(nilai_baru)

    def info(self):
        print(" Informasi Variabel")
        print(f"   Nilai : {self.nilai}")
        print(f"   Tipe  : {self.tipe._name_}")
        print("-" * 40)

    def to_str(self):
        return str(self.nilai)

    def tambah(self, angka):
        if isinstance(self.nilai, (int, float)) and isinstance(angka, (int, float)):
            hasil = self.nilai + angka
            print(f"+ Operasi tambah: {self.nilai} + {angka} = {hasil}")
            return hasil
        else:
            print(" Operasi tambah hanya untuk angka!")
            return None


# Contoh Penggunaan

var = VariabelDinamis(10)
var.info()

var.set("Sekarang string")
var.info()

var.set(3.5)
var.info()
var.tambah(2.5)

var.set(True)
var.info()

var.set([1, 2, 3])
var.info()