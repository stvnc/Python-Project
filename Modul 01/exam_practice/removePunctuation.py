import string

exclude = string.punctuation
newList = []

userInput = list(str(input('Masukkan kalimat yang diinginkan: ')))

for i in userInput:
    if i not in exclude:
        newList.append(i)
newString = ''.join(newList)
print(newString)


