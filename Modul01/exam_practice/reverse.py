def reverse(param):
    lengthBoundary = len(param)
    tempIndex = len(param)-1
    tempValue = 0
    newList = list(param)

    if lengthBoundary%2==1:
        for i in range(int(lengthBoundary/2)+1):
            tempValue = newList[i]
            newList[i] = newList[tempIndex]
            newList[tempIndex] = tempValue
            tempIndex -= 1
    else:
        for i in range(int(lengthBoundary/2)):
            tempValue = newList[i]
            newList[i] = newList[tempIndex]
            newList[tempIndex] = tempValue
            tempIndex -= 1

    return newList

def reverseWhile(param):
    paramLength = len(param)
    tempValue = 0
    tempIndex = len(param)-1
    newList = list(param)
    count = 0

    if paramLength%2 == 1:
        while(count < int(paramLength/2)+1):
            tempValue = newList[count]
            newList[count] = newList[tempIndex]
            newList[tempIndex] = tempValue
            count += 1
            tempIndex -= 1
    else: 
        while(count < int(paramLength/2)):
            tempValue = newList[count]
            newList[count] = newList[tempIndex]
            newList[tempIndex] = tempValue
            count += 1
            tempIndex -= 1

    return newList

userInput = str(input('Masukkan kata yang ingin direverse: '))

print(reverse(userInput))
print(reverseWhile(userInput))