
def factorial(x):
    temp = 1
    for i in range(1,x+1):
        temp *= i

    print(f'Hasil faktorial dari {x} adalah {temp}')
    
userInput = int(input("Masukkan angka yang diinginkan untuk difaktorial: "))
factorial(userInput)
