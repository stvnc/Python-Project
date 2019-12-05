'''
    Rasio umur Budi dan Andi adalah 4:10
    Total umur keduanya adalah 49
    Budi = 4/10 Andi
    Andi + 4/10 Andi = 49 ----- x10

    10 Andi + 4 Andi = 490
    14 Andi = 490
    Andi = 35

    Andi + Budi = 49
    35 + Budi = 49
    Budi = 14

    2 tahun lagi?
    Andi + 2 = 37
    Budi + 2 = 16
'''

rasioAndi = 4
rasioBudi = 10
totalUmur = 49

umurAndi = (totalUmur*rasioAndi)/(rasioAndi+rasioBudi)
print(f'Umur Andi: {umurAndi}')

umurBudi = (totalUmur*rasioBudi)/(rasioAndi+rasioBudi)
print(f'Umur Budi: {umurBudi}')

print(f'Umur Andi dan Budi 2 tahun yang akan mendatang: {umurAndi+2}, {umurBudi+2}')


