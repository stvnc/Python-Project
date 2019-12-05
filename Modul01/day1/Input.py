'''
nama = input('Halo, namamu siapa? : ')
print(f'Selamat datang, {nama}')

angka = int(input('Masukkan angka: '))
print(f'Kuadrat dari {angka} = {angka ** 2}')
'''

totalAnimal = int(input('Masukkan total hewan : '))
totalFeet = int(input('Masukkan total kaki hewan : '))
animal1Feet = int(input('Masukkan total kaki hewan pertama: '))
animal2Feet = int(input('Masukkan total kaki hewan kedua: '))

divisor = abs(animal2Feet-animal1Feet)
if divisor == 0:
    divisor = 1

animal1 = abs((totalFeet - (totalAnimal*animal2Feet)))/divisor #Untuk mengeliminasi 
print("Animal1:", animal1)

animal2 = (totalFeet - (animal1*animal1Feet))/animal2Feet
print("Animal2:", animal2)