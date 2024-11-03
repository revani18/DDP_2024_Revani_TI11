print("")
print("3. Buat program untuk minta input jumlah baris dan buat rangkaian berikut ini: *, **, ***, **** Dan seterusnya sejumlah baris yang diinputkan. Gunakan for loop dengan range")
print("")

baris = int(input('Masukkan baris: '))
for i in range (1, baris +1):
    print('*' *i)
print("")