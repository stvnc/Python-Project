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
        
