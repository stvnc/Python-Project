kodeMorse = { 
                'A':'.-', 'B':'-...', 
                'C':'-.-.', 'D':'-..', 'E':'.', 
                'F':'..-.', 'G':'--.', 'H':'....', 
                'I':'..', 'J':'.---', 'K':'-.-', 
                'L':'.-..', 'M':'--', 'N':'-.', 
                'O':'---', 'P':'.--.', 'Q':'--.-', 
                'R':'.-.', 'S':'...', 'T':'-', 
                'U':'..-', 'V':'...-', 'W':'.--', 
                'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', 
                '7':'--...', '8':'---..', '9':'----.', 
                '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-', ' ': '|'
            }

def morseCipher(param): # fungsi untuk melakukan enkripsi
    cipherString = ''

    for i in param:
        if i != ' ':
            cipherString += kodeMorse[i] + ' '
        else:
            cipherString += ' '
    return cipherString

def morseDecrypt(param): # fungsi untuk melakukan dekripsi 
    decryptedString = ''
    newList = param.split("|")
    
    for i in newList:
        if i in list(kodeMorse.values()):
            decryptedString += list(kodeMorse.keys())[list(kodeMorse.values()).index(i)] + ''
        else:
            decryptedString += ''
    return decryptedString

def checkIndex(param): # untuk mengambil index dari spasi
    indexList = []
    currentIndex = 0

    for i in range(currentIndex, len(param)):
        if param[i] == ' ':
            currentIndex = i
            indexList.append(currentIndex)
    return indexList

def stringJoin(param):
    for i in emptyList:
        param.insert(i, ' ')
    return ''.join(param)

def morseJoin(param):
    return ''.join(param)

numberInput = int(input('Ketik 1 untuk mengenkripsi String dan 2 untuk mendekripsi Morse: '))
if numberInput == 1:
    userInput = input('Masukkan kata yang ingin dienkripsi: ')
    emptyList = checkIndex(userInput)
    print(emptyList) 
            
    morseEncrypted = morseCipher(userInput.upper())
    print(f'Hasil Enkripsi dari {userInput}: {morseEncrypted}')

    morseDecrypted = stringJoin(list(morseDecrypt(morseEncrypted)))
    print(f'Hasil Dekripsi: {morseDecrypted}')

else:
    userInput = input('Masukkan kode morse yang ingin didekripsi: ')
    emptyList = checkIndex(userInput)

    morseDecrypted = morseJoin(list(morseDecrypt(userInput)))
    print(f'Hasil Dekripsi: {morseDecrypted}')


