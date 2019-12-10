data = [
    {'nama': 'Andi', 'usia': 21},
    {'nama': 'Budi', 'usia': 22},
    {'nama': 'Caca', 'usia': 23},
    {'nama': 'Deni', 'usia': 24}
]

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printValue(self):
        print(f'{self.name} {self.age}')

newDict = {}

for i in data:
    stud = student(i['nama'], i['usia'])
    stud.printValue()
    newDict[stud.name] = stud.age

print(newDict)

def createObj(param):
    nama = param['nama']
    vars()[nama] = student(param['nama'], param['usia'])
    return vars()[nama]

newData = list(map(createObj, data))
for i in newData:
    print(f'{i.name} {i.age}')

newData2 = list(map(lambda x: student(x['nama'], x['usia']), data))
for i in newData2:
    print(f'{i.name} {i.age}')