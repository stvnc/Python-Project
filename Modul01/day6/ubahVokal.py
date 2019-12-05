vocalWords = list('aiueo')

print(vocalWords)

def changeVocal(param):
    newString = ''
    for i in param:
        if i in vocalWords:
            i = 'o'
            newString += i
        else:
            newString += i
    print(newString)

changeVocal(str(input('Masukkan suatu kalimat: ')).lower())