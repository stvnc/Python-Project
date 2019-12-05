numberList = [
    [1, 2],
    [4, 5],
    [7, 8]
    ]

newList = [[numberList[j][i] for j in range(len(numberList))] for i in range(len(numberList[0]))] 

print(newList)

numList = [
    [12,7],
    [4 ,5],
    [3 ,8]
    ]
result = [
    [0,0,0],
    [0,0,0]
    ]
# iterate through rows
for i in range(len(numList)):
   # iterate through columns
   for j in range(len(numList[0])):
       result[j][i] = numList[i][j]
print(result)