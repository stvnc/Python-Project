class degreeConverter:
    def __init__(self, param):
        self.param = param

    def fromCelciusToFahrenheit(self):
        return (self.param * 9 / 5) + 32

    def fromFahrenheitToCelsius(self):
        return (self.param * 5 / 9) - 32

    def fromCelciusToKelvin(self):
        return self.param+273

    def fromKelvinToCelcius(self):
        return self.param-273

    def fromCelciusToReamur(self):
        return 4 * self.param /5

    def fromReamurToCelcius(self):
        return 5 * self.param /4

degreeDict = {
    'Celcius' : 1,
    'Fahrenheit' : 2,
    'Kelvin' : 3,
    'Reamur' : 4
}

print(degreeDict)

userInput = int(input('Masukkan kode temperatur yang ingin dikonversi: '))
userInput2 = int(input('Masukkan kode temperatur yang dituju: '))
degreeInput = float(input('Masukkan temperatur yang diinginkan: '))

degree = degreeConverter(degreeInput)

if userInput == 1 and userInput2 == 2:
    print('%0.2f' %degree.fromCelciusToFahrenheit())

elif userInput == 2 and userInput2 == 1:
    print('%0.2f' %degree.fromFahrenheitToCelsius())

elif userInput == 1 and userInput2 == 3:
    print('%0.2f' %degree.fromCelciusToKelvin())

elif userInput == 3 and userInput2 == 1:
    print('%0.2f' %degree.fromKelvinToCelcius())

elif userInput == 1 and userInput2 == 4:
    print('%0.2f' %degree.fromCelciusToReamur())

elif userInput == 4 and userInput2 == 1:
    print('%0.2f' %degree.fromReamurToCelcius())
