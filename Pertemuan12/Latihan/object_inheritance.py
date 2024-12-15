from mahasiswa import *
from dosen import *

m1 = mahasiswa('Siti Aminah', 'Wanita', 20, 'SI', 3)
m2 = mahasiswa('Budi Santoso', 'Pria', 23, 'TI', 5)
d1 = dosen('Sirojul Munir', 'Pria', 43, 'S.Si, M.Kom', 'LPPM')
d2 = dosen('Henry Saptono', 'Pria', 44, 'S.Si, M.Kom', 'LTSI')

d1.setGaji(12000000)
d2.setGaji(10000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()