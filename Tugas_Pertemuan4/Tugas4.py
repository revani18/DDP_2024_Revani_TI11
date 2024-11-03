#Soal 4: Cek Keanggotaan
#Buatlah program yang meminta pengguna untuk memasukkan status keanggotaan (misalnya "gold", "silver", atau "bronze"). Jika statusnya "gold" atau "silver", cetak "Selamat! Anda mendapatkan diskon". Gunakan if or.

status_keanggotaan = input("Masukkan Status Keanggotaan :").lower()

if status_keanggotaan == "gold" or status_keanggotaan == "silver" :
    print("Selamat! Anda mendapatkan diskon")
else :
    print("Maaf! Anda tidak mendapatkan diskon")