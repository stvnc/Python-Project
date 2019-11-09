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

def recursiveMultiplication(param, param2):
    temp = 1
    for i in range(param2):
        temp *= param
    return temp

def findFpb(param, param2):
    dict1 = dict(param)
    dict2 = dict(param2)
    temp = 1

    for i in list(dict1.keys()):
        if i in dict2.keys():
            if dict1[i] > dict2[i]:
                temp *=  recursiveMultiplication(i, dict2[i])
            else:
                temp *= recursiveMultiplication(i, dict1[i])
    return temp
            
userInput = int(input('Masukkan angka yang ingin dicek: '))
userInput2 = int(input('Masukkan angka yang ingin dicek: '))
setList = findSet(userInput)
newSetList = findSet(userInput2)
setPower = findPower(userInput, setList)
setPower2 = findPower(userInput2, newSetList)
print(findFpb(setPower, setPower2))
print(setList)
print(findPower(userInput, setList))
print(printFactor(userInput))
