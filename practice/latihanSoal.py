# 3x + 2y = 11000
# x  + 3y = 9500
# c = ?
#substitusi = x = 9500 - 3y
totalHarga1 = 11000
totalHarga2 = 9500
rasioBukuAndi = 3
rasioPenAndi = 2

hargaPen = ((3*totalHarga2)-totalHarga1)/(rasioBukuAndi ** 2 - rasioPenAndi)
hargaBuku = (totalHarga1 - (rasioPenAndi * hargaPen))/rasioBukuAndi
print(hargaPen)
print(hargaBuku)