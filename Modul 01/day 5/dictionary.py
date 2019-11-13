# -------------------------- Jumat, 25 Oktober 2019 -----------------------------------

# Dictionary or object
andi = {
    'name': 'Andi', 
    'age' : 22, 
    'is_married' : False,
    'cars' : ['Alphard', 'Xpander', 'Innova'],
    'address' :{
        'street' : 'Mawar Ungu',
        'RT' : 5, 'RW' : 12, 'Kecamatan' : 'x',
        'zipcode' : 14045,
        'geo' : {
            'lat' : 111.11,    # Latitude
            'lng' : 65.89      # Longitude
        }
    }
}

print(andi['name'])         # nama list [index], 
print(andi['age'])
print(andi['is_married'])

### 'name' , 'age', 'is_married', 'cars', =  merupakan 'keys'
### konten di dalam 'keys' adalah 'values'

# contoh lain
print(andi.get('name'))
print(andi.get('age'))
print(andi.get('is_married'))
print(andi.get('job', 'Maaf Andi masih menganggur'))

# Perbedaan bila (andi['job']) dengan (andi.get('job')), untuk '.get' tidak mengalami 
# eror bila 'keys' tidak ada di dalam data

# untuk me-replace elemen di dalam data
andi['name'] = 'Budi'
print(andi)

print(andi['cars'])
print(andi['cars'][0])

# meng-extract informasi dari 'address'
print(andi['address']['geo'])

# Untuk mengetahui 'keys' di dalam dictionary
print(list(andi))
print(list(andi.keys()))

# Untuk mengetahui 'values' di dalam dictionary
print(list(andi.values()))

# Untuk menambahkan elemen
andi['salary'] = 25000000
andi.update({'no_ktp' : 234089})
print(andi)

# Untuk memperlihatkan semua konten yg ada di dalam 'set'
x = {1: True, 2: False}
print(list(x.items()))