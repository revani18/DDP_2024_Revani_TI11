class Gempa:
    # Konstruktor inisialisasi atribut lokasi dan skala
    def __init__(self, lokasi, skala):
        
        # Atribut
        self.lokasi = lokasi
        self.skala = skala

    # Method, Menentukan dampak gempa
    def dampak(self):
        
        # Statement / Logika
        if self.skala < 2 :
            print("Dampak gempa tidak berasa")
        elif self.skala >= 2 and self.skala <= 4 :
            print("Dampak gempa bangunan retak-retak")
        elif self.skala > 4 and self.skala <= 6 :
            print("Dampak gempa bangunan roboh")
        elif self.skala > 6 :
            print("Dampak gempa bangunan roboh dan berpotensi tsunami")

        # Menampilkan lokasi dan skala
        print(f"Lokasi Gempa : {self.lokasi} ")
        print(f"Skala Gempa : {self.skala} ")