#  ------------------------ Jumat, 8 November 2019 -----------------------------------

# Membuka data di python
data = open('data.txt', 'r')

# r = read / asking
# w = write / re-write / membuat file baru
# a = append


# Untuk mengecek apakah file tsb readable
# print(data.readable())
# # print(data.read())
# print(data.readlines())

data = open('data.txt', 'w')
data.write('Test 1 2 3')
data.write('\nCoding Python')

data = open('data.txt', 'a')
data.write(' \nhalo\n')
'''
Contoh untuk membuat file python
data = open('data.py', 'w')
data.write("print('ok')")   # dijadikan str yg mau ditambahkan
'''

# Untuk menginput codingan python ke dari file text (data2.txt) ke dalam file python (data.py)
# Kemudian codingan tsb dapat dijalankan
# data2 = open('data2.txt', 'r')
# x = data2.read()

# data2 = open('data.py', 'a')
# data2.write(x)


#########################################################
# Bertujuan untuk memindah konten di dalam data3.txt ke dalam data.txt
# Dari Andi, Budi, Caca  menjadi
# Caca
# Budi
# Andi


data3 = open('data3.txt' , 'r')
y = data3.read()      # atau data3.read().split(', ').[::-1]
y = y.split()      
# print(y)

# y = y[::-1]
y.reverse()
# print(y)

data3 = open('data.txt', 'w')
for i in y:
    data.write(i + '\n')


##########################################
# Mirip sepeti dataquest.io
# Cara membuka file '.csv' lalu di rubah menjadi dictionary

filecsv = open('file.csv', 'r')
filecsv = filecsv.read()
# print(filecsv)

filecsv = filecsv.split()
print(filecsv)

csv = []
for i in filecsv:
    editcsv = i.split(',')
    csv.append(editcsv)

print(csv)

list_header  = csv[0]
list_content = csv[1:]
# x = len(list_header)
# print(x)

# Menggunakan 'zip' untuk menambahkan 'keys' dan 'value' ke dalam dictionary
dataDiri = []
for i in range(len(list_header)):
    y = dict(zip(list_header, list_content[0:][i]))
    dataDiri.append(y)

print(dataDiri)

############################################
# Validate json  , , jsonlint.com

############################################
# Cara lain membuka file '.csv' dan merubahnya menjadi dictionary
import csv

# Cara 1
with open('file.csv', 'r') as dataX:
    baca = csv.reader(dataX)
    print(list(baca))

# Cara 2
with open('file.csv', 'r') as dataX:
    baca = csv.DictReader(dataX)
    konten = []
    for i in baca:
        konten.append(dict(i))
print(konten)

#############################################
# Dapat pula me-write file '.csv', menulis/memasukkan dictionary ke dalam konten '.csv' 

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


#############################################
