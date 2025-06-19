# Class adalah template atau cetakan untuk membuat objek.
# # Bayangkan class seperti desain blueprint rumah.

class Manusia:
    # class variable (milik semua manusia)
    kebutuhan = ["udara", "air", "makanan"]

    def __init__(self, nama):
        # instance variable (hanya milik 1 orang)
        self.nama = nama

# Instance adalah objek nyata yang dibuat dari class.
# Kalau class adalah cetakan, maka instance adalah produk nyatanya.

john = Manusia("John")  # john adalah instance dari class Manusia
jane = Manusia("Jane")  # jane juga instance, tapi berbeda dengan john
