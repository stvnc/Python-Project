'''
    Andi + Ayah = 50
    6(Andi - 4) = Ayah - 4
    
    6Andi - 24 = Ayah - 4
    6 Andi - Ayah = 20

    Andi + Ayah = 50
    6Andi - Ayah = 20
    -----------------  +
    7Andi        = 70
    Andi         = 10

    Ayah = 40 , Andi = 10
'''

totalUmur = 50
rasioUmurAndi = 1
rasioUmurAyah = 6
jumlahTahun = 4

#umur4TahunLalu = (totalUmur-8)/(rasioUmurAndi+rasioUmurAyah)
#umurAndi = umur4TahunLalu+4
#umurAyah = 6*umur4TahunLalu+4

umurAyah = (rasioUmurAyah*(totalUmur-jumlahTahun)+jumlahTahun)/(rasioUmurAndi+rasioUmurAyah)
umurAndi = totalUmur - umurAyah

print(f'Umur Andi adalah {umurAndi}')
print(f'Umur Ayah adalah {umurAyah}')



