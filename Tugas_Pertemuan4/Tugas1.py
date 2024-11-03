#Soal 1: Bilangan Genap atau Ganjil
#Buatlah program yang meminta pengguna untuk memasukkan sebuah bilangan bulat. Program harus menentukan apakah bilangan tersebut genap atau ganjil menggunakan if dan if else.

bilangan_bulat = int(input("Masukkan bilangan bulat: "))

if bilangan_bulat %2==0:
    print("Bilangan", bilangan_bulat,"adalah bilangan genap")
else :
    print("Bilangan", bilangan_bulat,"adalah bilangan ganjil")

run_again = input("Apakah anda ingin menjalankan program ini lagi?")

if run_again != 'y':
    print("Program selesai")