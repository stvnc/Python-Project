userInput = int(input('Masukkan angka yang diinginkan: '))

for i in range(1, userInput+1):
    newString = ''
    for j in range(1, i+1):
        newString += str(j)
    print(newString)

print()

for i in range(userInput, 0, -1):
    newString = ''
    for j in range(i,0,-1):
        newString += str(j)
    print(newString)

