#Soal 5: Pembelian Diskon
#Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.
#example : 
#minyak 25.000, indomie 5.000, beras 75.000, gula 25.000, kopi 20.000, teh 10.000

minyak = 25000
indomie = 5000

#input
jumlah_pembelian_minyak = int(input("Masukkan jumlah pembelian minyak:"))
jumlah_pembelian_indomie = int(input("Masukkan jumlah pembelian indomie:"))

#proses
total_harga = (jumlah_pembelian_minyak*minyak)+(jumlah_pembelian_indomie*indomie)
diskon = 0.1

#shorthandif
total_diskon = total_harga*diskon if(jumlah_pembelian_minyak + jumlah_pembelian_indomie) > 100 else 0
total_harga -= total_diskon

#cetakhasil
print("Diskon yang anda dapatkan sebesar 10% Rp",total_diskon if total_diskon > 0 else "Tidak ada diskon")
print("Total harga : Rp", total_harga)
