class Animal:
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak
    
    # method informasi
    def info_animal(self):
        print(f"Nama Hewan\t\t: ", self.nama, "\nMakanan\t\t\t: ", self.makanan, "\nHidup\t\t\t: ", self.hidup, "\nBerkembang Biak\t\t: ", self.berkembangbiak)

# Objek
# kucing = Animal("Kucing", "Daging", "Hidup", "Melahirkan")
# kucing.info_animal()

# buaya = Animal('Buaya', 'daging', 'perairan tawar', 'bertelur')
# buaya.info_animal()

# jerapah = Animal('Jerapah', 'daun', 'darat', 'melahirkan')
# jerapah.info_animal()
