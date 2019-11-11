numberList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

newList = [[numberList[j][i] for j in range(len(numberList))] for i in range(len(numberList))] 

print(newList)