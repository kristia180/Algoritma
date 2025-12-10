class UserStatus:
    STATUS_VALID = ["online", "offline", "busy", "idle", "away"]

    def _init_(self, nama):
        self.nama = nama
        self.status = "offline"

    def set_status(self, new_status):
        if new_status in self.STATUS_VALID:
            print(f" {self.nama} mengubah status: {self.status} → {new_status}")
            self.status = new_status
        else:
            print(f" Status '{new_status}' tidak diperbolehkan!")

    def get_status(self):
        print(f" {self.nama} saat ini berstatus: {self.status}")

    def is_online(self):
        return self.status == "online"

    def reset_status(self):
        print(f"🔄 {self.nama} mereset status ke 'offline'")
        self.status = "offline"


# Contoh penggunaan

user = UserStatus("Cristia")

user.get_status()
user.set_status("online")
user.get_status()

print("Apakah user online?", user.is_online())
print()

user.set_status("busy")
user.get_status()

print()

user.set_status("tidur")  # tidak valid
user.reset_status()
user.get_status()