import random

userInput = int(input('Masukkan angka yang diinginkan: '))

randomList = []

for i in range(userInput):
    randomList.append(random.randint(0,20))

def mean(param):
    length = len(param)
    tempVal = 0
    for i in param:
        tempVal += i

    return (tempVal/length)

print(f'Mean dari {randomList} adalah {mean(randomList)}')