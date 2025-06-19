class Mobil:
    jumlah_roda = 4 #class variable (sama untuk semua mobil)

    def __init__(self, warna):
        self.warna = warna #instance variable (unik per mobil)

#membuat dua mobil

mobil1 = Mobil("merah")
mobil2 = Mobil("biru")

print(f"mobil 1 warna : {mobil1.warna}")
print(f"mobil 2 warna : {mobil2.warna}")
print(f"jumlah roda mobil1 :{mobil1.jumlah_roda}")
print(f"jumlah roda mobil2 :{mobil2.jumlah_roda}")
print(f"jumlah roda (class) : {Mobil.jumlah_roda}")

mobil1.jumlah_roda=3
print("setelah di ubah")

print(f"jumlah roda mobil1 :{mobil1.jumlah_roda}")
print(f"jumlah roda mobil2 :{mobil2.jumlah_roda}")
print(f"jumlah roda (class) : {Mobil.jumlah_roda}")

# 📌 Penjelasan
# Saat kamu tulis mobil1.jumlah_roda = 3, kamu membuat instance variable baru,
# jadi hanya mobil1 yang berubah, sedangkan mobil2 dan Mobil tetap 4.

Mobil.jumlah_roda = 6

print("setelah di ubah")

print(f"jumlah roda mobil1 :{mobil1.jumlah_roda}")
print(f"jumlah roda mobil2 :{mobil2.jumlah_roda}")
print(f"jumlah roda (class) : {Mobil.jumlah_roda}")

# | Hal                                       | Instance Variable (`self.warna`) | Class Variable (`Mobil.jumlah_roda`) |
# | ----------------------------------------- | -------------------------------- | ------------------------------------ |
# | Berlaku untuk siapa                       | Satu objek saja                  | Semua objek dari class-nya           |
# | Diakses pakai apa                         | `self`                           | `cls` atau langsung dari class       |
# | Bisa diubah di mana?                      | Di dalam objek                   | Di dalam class                       |
# | Apa yang terjadi kalau diubah di 1 objek? | Objek itu saja yang terpengaruh  | Semua objek ikut berubah             |

