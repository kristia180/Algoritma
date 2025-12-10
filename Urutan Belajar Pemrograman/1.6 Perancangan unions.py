class UnionEnhanced:
    def _init_(self):
        self.value = None
        self.tipe = None

    def set(self, nilai_baru):
        self.value = nilai_baru
        if isinstance(nilai_baru, int):
            self.tipe = "integer"
        elif isinstance(nilai_baru, float):
            self.tipe = "float"
        elif isinstance(nilai_baru, str):
            self.tipe = "string"
        else:
            self.tipe = "unknown"

        print(f"✔ Nilai berubah menjadi: {self.value}")
        print(f"  Tipe terdeteksi: {self.tipe}")
        print("-" * 40)

    def tambah(self, angka):
        if isinstance(self.value, (int, float)) and isinstance(angka, (int, float)):
            hasil = self.value + angka
            print(f" {self.value} + {angka} = {hasil}")
            return hasil
        else:
            print(" Tidak bisa menambah: nilai bukan angka!")
            return None

    def uppercase(self):
        if isinstance(self.value, str):
            hasil = self.value.upper()
            print(" Uppercase →", hasil)
            return hasil
        else:
            print(" Nilai bukan string!")
            return None

    def reset(self):
        print(" Reset union: nilai dikosongkan.")
        self.value = None
        self.tipe = None

    def info(self):
        print(" INFO UNION")
        print("   Nilai :", self.value)
        print("   Tipe  :", self.tipe)
        print("=" * 40)


# Contoh penggunaan

u = UnionEnhanced()

u.set(100)
u.tambah(50)
u.info()

u.set("hello union")
u.uppercase()
u.info()

u.set(3.14)
u.tambah(2)
u.info()

u.reset()
u.info()