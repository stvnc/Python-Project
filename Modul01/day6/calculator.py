def add(x, y):
    print(f'Hasil pertambahan {x} dan {y} adalah: {x+y}')

def subtract(x, y):
    print(f'Hasil pengurangan {x} dan {y} adalah {x-y}')

def multiply(x, y):
    print(f'Hasil pengalian {x} dan {y} adalah {x*y}')
    
def division(x, y):
    print(f'Hasil pembagian {x} dan {y} adalah {x/y}')

def modulus(x, y):
    print(f'Hasil modulus {x} dan {y} adalah {x%y}')

def power(x, y):
    print(f'Hasil pembagian {x} dan {y} adalah {x ** y}')

input1 = float(input("Masukkan angka pertama: "))
print("Operator aritmetika yang tersedia: +, -, *, /, %, **")
inputArithmeticOperator = input("Masukkan operator aritmetik yang diinginkan: ")
input2 = float(input("Masukkan angka kedua: "))

if inputArithmeticOperator == '*':
    multiply(input1, input2)
elif inputArithmeticOperator == '+':
    add(input1, input2)
elif inputArithmeticOperator == '/':
    division(input1, input2)
elif inputArithmeticOperator == '**':
    power(input1, input2)
elif inputArithmeticOperator == '-':
    subtract(input1, input2)
elif inputArithmeticOperator == '%':
    modulus(input1, input2)
else:
    print('Operator tidak dikenal')






