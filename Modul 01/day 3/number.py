import math

print(math.pi)
print(math.floor(3.9)) #pembulatan kebawah
print(math.ceil(3.9)) #pembulatan keatas
print(math.sqrt(196))
print(math.factorial(5))

# kambing + ayam = 13
# 4 kambing + 2 ayam = 32
totalAnimal = 13
totalFeet = 32
animal1Feet = 2
animal2Feet = 4

divisor = abs(animal2Feet-animal1Feet)
if divisor == 0:
    divisor = 1

goat = abs((totalFeet - (totalAnimal*animal1Feet)))/divisor #Untuk mengeliminasi chicken
print("Goat:", goat)

chicken = (totalFeet - (goat*animal2Feet))/animal1Feet
print("Cow:", chicken)


'''

chicken = (goatFeet*totalAnimal - totalFeet)/chickenFeet
print("Chicken:", chicken)

goat = totalAnimal - chicken
print("Goat:", goat)
'''

totalKendaraan = 20
totalRoda = 75
rodaBajaj = 3
rodaMobil = 4

divisor = abs(rodaMobil-rodaBajaj)
if divisor == 0:
    divisor = 1

bajaj = abs((totalRoda - (totalKendaraan*rodaMobil)))/divisor #Untuk mengeliminasi chicken
print("bajaj:", bajaj)

mobil = (totalRoda - (bajaj*rodaBajaj))/rodaMobil
print("mobil:", mobil)
