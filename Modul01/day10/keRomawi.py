class romanClass():
    def __init__(self, number):
        self.number = number
    
romanDict = {
    'M' : 1000,
    'CM': 900,
    'D' : 500,
    'CD': 400,
    'C' : 100,
    'XC': 90,
    'L' : 50,
    'XL': 40,
    'X' : 10,
    'IX': 9,
    'V' : 5,
    'IV': 4,
    'I' : 1
}

def romanNumeral(param):
    newString = ''
    while param > 1:
        for i in list(romanDict.values()):
            newString += (int(param/i) * list(romanDict.keys())[list(romanDict.values()).index(i)])
            param %= i
    print(newString)

romanNumeral(int(input('Masukkan angka yang ingin diubah ke numeral Roman: ')))

def romanDecipher(param):
    newList = list(param)
    count = 0
    value = 0
    if len(param) == 1:
        value += romanDict.get(newList[count])
    while count < len(param)-1:
        if newList[count] in romanDict:
            if romanDict.get(newList[count]) > romanDict.get(newList[count+1]):
                value += romanDict.get(newList[count])
            elif romanDict.get(newList[count]) < romanDict.get(newList[count+1]):
                value -= romanDict.get(newList[count])
            else:
                value += romanDict.get(newList[count])
            count += 1
            if count == len(param)-1 :
                value += romanDict.get(newList[count])
            
    return value

print(romanDecipher(str(input('Masukkan numeral Roman yang ingin dijadikan angka: ')).upper()))