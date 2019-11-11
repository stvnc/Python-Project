numberList = [
    [1, 2],
    [4, 5],
    [7, 8]
]

newList = [[numberList[j][i] for j in range(len(numberList))] for i in range(len(numberList[0]))] 

print(newList)