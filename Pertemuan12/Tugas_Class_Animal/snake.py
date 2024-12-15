from animal import Animal

class Snake(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembangbiak, warna, jenis):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.warna = warna
        self.jenis = jenis
    
    # Method
    def info_snake(self):
        super().info_animal()
        print(f"Warna\t\t\t: ", self.warna, "\nJenis Ular\t\t: ", self.jenis)


# Objek
print()
snake = Snake("Ular Sanca", "Daging", "hutan, padang rumput, semak belukar, perkebunan", "Bertelur", "Coklat Kehitaman", "Ular Berbisa")
print("## Info Ular 1 ##")
snake.info_snake()

print()
snake = Snake("Ular Kobra", "Berbagai Jenis Makanan", "Di tempat yang gelap dan sembap", "Bertelur", "Abu-Abu Kehitaman", "Ular Berbisa")
print("## Info Ular 2 ##")
snake.info_snake()

print()
snake = Snake("Ular Sanca", "Daging", "sabana, hutan gersang, bukit berbatu, dan lembah", "Bertelur", "Hitam", "Ular Berbisa")
print("## Info Ular 3 ##")
snake.info_snake()
print()