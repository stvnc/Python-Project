alphabet = list('abcdefghijklmnopqrstuvwxyz')

word = "Claudia Audi Susanto"

wordReplace = list(word.lower().replace(" ", ""))

def bubbleSort(param):
    for i in range(len(param),0,-1):
        for j in range(0, i-1):
            if param[j] > param[j+1]:
                param[j], param[j+1] = param[j+1], param[j]
    return param

print(bubbleSort(wordReplace))

splitWord = word.split()

temp = 0
for i in range(len(splitWord),0,-1):
    for j in range(0,-1):
        if splitWord[j] > splitWord[j+1]:
            splitWord[j], splitWord[j+1] = splitWord[j+1], splitWord[j]
    
print(splitWord)

l = ['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2']
numbersPerLetter = 2
lsorted = []
for i in range(len(l) / numbersPerLetter):
   lsorted.extend([l[x+i] for x in range(0, len(l), len(l) / numbersPerLetter)])
print(lsorted)
        

