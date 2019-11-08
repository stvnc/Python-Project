divisorList = [2, 3, 5, 7, 11, 13, 17, 19]

def findSet(param):
    newList = []
    for i in divisorList:
        if (param % i) == 0:
            newList.append(i)
    return newList

def findPower(param, param2):
    powerDict = {}
    for i in param2:
        temp = param
        count = 0
        status = True
        powerDict.setdefault(i, 1)
        while status == True:
            if temp%i==0:
                temp /= i
                count += 1
            else:
                status = False
        powerDict[i] = count
    return powerDict

def printFactor(param):
    newList = []
    for i in range(1, param+1):
        if param % i == 0:
            newList.append(i)
    return newList            

userInput = int(input('Masukkan angka yang ingin dicek: '))
setList = findSet(userInput)
print(setList)
print(findPower(userInput, setList))
print(printFactor(userInput))
