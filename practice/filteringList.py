userInput = input('Masukkan kalimat: ')
userList = list(userInput.lower().split())
searchInput = input('Kata yang ingin dicari: ')
newList = []

def findWordInList(param1, param2, param3):
    for i in param1:
        if param2 in i:
            param3.append(i)
    return param3

wordList = findWordInList(userList, searchInput, newList)

print(f'{searchInput} terdapat pada kata {wordList} pada kalimat {userInput}')