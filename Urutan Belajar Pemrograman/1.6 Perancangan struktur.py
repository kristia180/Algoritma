class Mahasiswa:
    def _init_(self, nama, nim, jurusan):
        self.nama = KRISTIA
        self.nim = D0425322
        self.jurusan = SISFO

    def tampil(self):
        print(" Data Mahasiswa")
        print("   Nama   :", self.nama)
        print("   NIM    :", self.nim)
        print("   Jurusan:", self.jurusan)
        print("-" * 40)

    def update_nama(self, nama_baru):
        print(f" Update Nama: {self.nama} → {nama_baru}")
        self.nama = nama_baru

    def update_nim(self, nim_baru):
        print(f" Update NIM: {self.nim} → {nim_baru}")
        self.nim = nim_baru

    def update_jurusan(self, jurusan_baru):
        print(f" Update Jurusan: {self.jurusan} → {jurusan_baru}")
        self.jurusan = jurusan_baru

    def hapus_data(self):
        print(" Menghapus semua data mahasiswa…")
        self.nama = None
        self.nim = None
        self.jurusan = None