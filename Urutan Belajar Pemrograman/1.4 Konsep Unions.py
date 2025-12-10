class UnionEnhanced:
    def _init_(self):
        self.value = None
        self.tipe = None

    def set(self, value):
        """Mendeteksi tipe otomatis"""
        self.value = value
        if isinstance(value, int):
            self.tipe = "integer"
        elif isinstance(value, float):
            self.tipe = "float"
        elif isinstance(value, str):
            self.tipe = "string"
        else:
            self.tipe = "unknown"

    def reset(self):
        print(" Semua nilai direset...")
        self.value = None
        self.tipe = None

    def get_info(self):
        print(" Informasi Union")
        print(f"   Nilai : {self.value}")
        print(f"   Tipe  : {self.tipe}")
        print("=" * 40)

    def as_upper(self):
        if isinstance(self.value, str):
            return self.value.upper()
        return " Nilai bukan string"

    def add(self, x):
        if isinstance(self.value, (int, float)) and isinstance(x, (int, float)):
            return self.value + x
        return " Tidak bisa melakukan operasi tambah."

# Contoh Penggunaan

u = UnionEnhanced()

u.set(100)
u.get_info()
print("Tambah 50 →", u.add(50))
print()

u.set("hello union python")
u.get_info()
print("Uppercase →", u.as_upper())
print()

u.reset()
u.get_info()