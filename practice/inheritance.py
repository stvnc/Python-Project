'''
class Person:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName

    def printName(self):
        print(self.firstName)
        print(self.lastName)
    
    def printWelcome(self):
        print(f'Hello, {self.firstName} {self.lastName}')

personInput = Person(input("Input nama pertama: "), input('Input nama kedua: '))
personInput.printName()
personInput.printWelcome()
'''

class Vehicle:
    def __init__(self, tWheels, vType):
        self.totalWheels = tWheels
        self.vehicleType = vType

class Car(Vehicle):
    def __init__(self, tWheels, vType, bName, bModel, cEngine, yMade):
        super().__init__(tWheels, vType)
        self.brandName = bName
        self.brandModel = bModel
        self.carEngine = cEngine
        self.yearMade = yMade

    def printDetails(self):
        print(f'\nTotal Wheels: {self.totalWheels}')
        print(f'Vehicle Type: {self.vehicleType}')
        print(f'Brand Name: {self.brandName}')
        print(f'Brand Model: {self.brandModel}')
        print(f'Car Engine: {self.carEngine} cc')
        print(f'Manufacture Year: {self.yearMade}')

class Motorcycle(Vehicle):
    def __init__(self, tWheels, vType, bName, bModel, mEngine, yMade):
        super().__init__(tWheels, vType)
        self.brandName = bName
        self.brandModel = bModel
        self.motorEngine = mEngine
        self.yearMade = yMade

    def printDetails(self):
        print(f'\nTotal Wheels: {self.totalWheels}')
        print(f'Vehicle Type: {self.vehicleType}')
        print(f'Brand Name: {self.brandName}')
        print(f'Brand Model: {self.brandModel}')
        print(f'Motorcycle Engine: {self.motorEngine} cc')
        print(f'Manufacture Year: {self.yearMade}')

print('Choose between Car and Motorcycle')

userInput = input('Input: ')

if userInput == 'Car':
    carInput = Car(4, 'Car', input('Brand name: '), input('Brand model: '),
        input('Car engine: '), input('Manufacture date: '))
    carInput.printDetails()
elif userInput == 'Motorcycle':
    motorInput = Motorcycle(2, 'Motorcycle', input('Brand name: '), input('Brand model: '),
        input('Motorcycle engine: '), input('Manufacture date: '))
    motorInput.printDetails()
else:
    print(f'{userInput} is not valid')





    

