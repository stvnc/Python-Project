newList = []
newList.append(int(input('Input 3 Numbers that you desire: ')))
newList.append(int(input('2: ')))
newList.append(int(input('3: ')))
print(newList)

def findMaxMin(param):
    temp = 0
    mmList = []
    for i in range(len(param), 0, -1):
        for j in range(0, i-1):
                if param[j] > param[j+1]:
                    temp = param[j]
                    param[j] = param[j+1]
                    param[j+1] = temp

    print(param)
    mmList.append(param[0])
    mmList.append(param[-1])
    return mmList

tempValue = findMaxMin(newList)
print(f'Max: {tempValue[1]}, Min: {tempValue[0]}')