#  ------------------------ Jumat, 8 November 2019 -----------------------------------

import csv
data = [
    {'nama':'Anton', 'umur':10, 'pendidikan':'SD'},
    {'nama':'Boni', 'umur':13, 'pendidikan':'SMP'},
    {'nama':'Cepi', 'umur':16, 'pendidikan':'SMA'}
]

with open('0.csv', 'w', newline='') as isi:
    kolom = ['nama', 'umur', 'pendidikan']
    abc = csv.DictWriter(isi, fieldnames=kolom)
    abc.writeheader()
    abc.writerows(data)

# Menggunakan extension '.json'
# Pada format '.json' untuk type string dipakai "" bukan ''

import json

# Membaca file json
# Versi ringkas merubah konten file '.json' menjadi dictionary di dalam list,

inside = open("a1.json", "r")
out = json.load(inside)
print(out)

# Membuat file '.json' yg baru menggunakan konten file yg lain / meng-clone
# with open('A2.json', 'w') as isi:
#     json.dump(out, y)

'''
manual / pakai package .csv .json:
1. .csv  => .json
2. .json => .csv
'''