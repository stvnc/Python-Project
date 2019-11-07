import random
from collections import Counter

userInput = int(input('Masukkan angka yang diinginkan: '))

randomList = []

for i in range(userInput):
    randomList.append(random.randint(0,20))

print(randomList)

'''
def findMode(param):
    counter = Counter(param)
    maxCount = max(counter.values())
    mode = [k for k,v in counter.items() if v == maxCount]
    return mode

print(f'Modus dari {randomList} adalah {findMode(randomList)}')
'''
'''
def getMode(param):
    countList = []
    for i in param:
        check = False
        for j in countList:
            if j[0] == i:
                j[1] += 1
                check = True
        if check == False:
            countList.append([i, 0])

    maxFreq = 0
    mode = []
    for i in countList:
        if i[1] > maxFreq:
            mode = [i[0]]
            maxFreq = i[1]
        else:
            mode.append(i[0])

    if len(mode) == len(countList):
        mode = []
    return mode

print(getMode(randomList))
'''
def findMode(param):
    paramDict = {}
    maxCount = 0
    for i in param:
        paramDict.setdefault(i, 0)
        paramDict[i] += 1
    print(paramDict)
    
    for i in paramDict:
        if maxCount < paramDict[i]:
            maxCount = i
    return maxCount
print(f'Modus = {findMode(randomList)}')
    