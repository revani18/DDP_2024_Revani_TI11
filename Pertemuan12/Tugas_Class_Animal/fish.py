from animal import Animal

class Fish(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembangbiak, bernapas, habitat):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.bernapas = bernapas
        self.habitat = habitat
    
    # Method
    def info_fish(self):
        super().info_animal()
        print(f"Bernapas Menggunakan\t: ", self.bernapas, "\nHabitat di\t\t: ", self.habitat)


# Objek
print()
fish = Fish("Ikan Hiu", "Daging", "Laut", "Melahirkan", "Insang", "Air Asin")
print("## Info Fish 1 ##")
fish.info_fish()

print()
fish = Fish("Ikan Piranha", "Berbagai Jenis Makanan", "Sungai", "Bertelur", "Insang", "Air Tawar")
print("## Info Fish 2 ##")
fish.info_fish()

print()
fish = Fish("Ikan Aligator", "Berbagai Jenis Makanan", "Sungai dan Danau", "Bertelur", "Insang", "Air Tawar, Payau, dan Asin")
print("## Info Fish 3 ##")
fish.info_fish()
print()