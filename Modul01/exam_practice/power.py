def power(param, param2): #Using For
    temp = 1
    for i in range(param2):
        temp *= param
    return temp

from functools import reduce
def powerLambda(param, param2): #Using Lambda
    newList = []
    for i in range(param2):
        newList.append(param)
    returnValue = reduce(lambda a,b: a*b, newList)
    return returnValue

def powerWhile(param, param2): #Using While
    count = 0
    temp = 1
    while(count < param2):
        temp *= param
        count += 1
    return temp

userInput = int(input('Masukkan angka yang ingin dipangkatkan: '))
powerInput = int(input('Masukkan angka yang ingin dijadikan pangkat: '))

print(power(userInput, powerInput))
print(powerLambda(userInput, powerInput))
print(powerWhile(userInput, powerInput))