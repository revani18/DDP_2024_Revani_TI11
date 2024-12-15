from animal import Animal

class Bird (Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembangbiak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.warna = warna
        self.paruh = paruh
    
    # Method
    def info_bird(self):
        super().info_animal()
        print(f"Warna\t\t\t: ", self.warna, "\nJenis Paruh \t\t: ", self.paruh)


# Objek
print()
bird = Bird("Burung Elang", "Biji", "10 Tahun", "Menghasilkan Telur", "Coklat", "Bengkok dan Lancip")
print("## Info Bird 1 ##")
bird.info_bird()

print()
bird = Bird("Burung Merpati", "Biji", "6 Tahun", "Menghasilkan Telur", "Abu-Abu", "Lancip")
print("## Info Bird 2 ##")
bird.info_bird()

print()
bird = Bird("Burung Hantu", "Daging", "30 Tahun", "Menghasilkan Telur", "Coklat", "Bengkok dan Lancip")
print("## Info Bird 3 ##")
bird.info_bird()
print()