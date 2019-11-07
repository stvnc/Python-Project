import random

userInput = int(input('Masukkan angka yang diinginkan: '))

randomList = []
medianValue = 0

for i in range(userInput):
    randomList.append(random.randint(0,20))

def median(param):
    param = sorted(param)
    print(param)
    length = len(param)
    if(length%2==1):
        medianValue = param[int(length/2)+1]
    else:
        medianValue = (param[int(length/2)-1] + param[int(length/2)]) / 2

    return medianValue

print(f'Median dari {randomList} adalah {median(randomList)}')