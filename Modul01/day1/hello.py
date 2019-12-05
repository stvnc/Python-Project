# Python Operand Test

x = 0
y = 20
c = 'hahaha'

if x > y:
    print('invalid')
else:
    print('valid')

print(c.islower()) #check if the string is lower case, if upper = .isupper
print(c.replace('hahaha', 'hehehe')) #replace string with another value

#.upper() -> change string to UPPERCASE

#Training Module

nama = 'Purwadhika Startup & Coding School'

#length dari kalimat
print("Length :", len(nama))

#length dari kalimat without whitespace
print("Length without whitespace", len(nama.replace(" ", "")))

#Jumlah huruf
#1st method - For Loop
count = 0
for i in nama.lower():
    if(i == 'c'):
        count = count + 1
print('Jumlah c : ', count)

#2nd method - Count
count = 0
count = nama.lower().count('c')
print('Jumlah c 2nd method: ', count)

#3rd method - If Expression
count = 0
temp = nama.lower().index('c')
if(temp > 0):
    count = count + 1
temp = nama[temp:len(nama)].index('c')
if(temp > 0):
    count = count + 1
print('Jumlah c 3rd method: ', count)

#4th method
cari = 'c'
x = nama.lower().replace(cari, '')
print(x)
jumlahCari = len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {jumlahCari}')

#Jumlah kata startup
#1st method
wordCounter = nama.lower().count('startup')
print('Jumlah kata startup :', wordCounter)

#2nd method
yangDicari = 'startup'
x =  nama.lower().replace(yangDicari, '')
jumlahCari = len(nama) -  len(x)
print(f'Jumlah kata \'{yangDicari}\' ada = {int(jumlahCari/len(yangDicari))}')


''' def cariIndex(list, i):
        return [x for x, y in enumerate(list) if y == i]

        print(cariIndex(a, 3))
'''