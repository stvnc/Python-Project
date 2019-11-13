def fiboList(param):
    fibonacciList = [1,1] # initialnya adalah 1 dan 1 
    for i in range(2, param):
        fibonacciList.append(fibonacciList[i-2] + fibonacciList[i-1])
        print(fibonacciList[i])
    return fibonacciList[param-1]

userInput = int(input('Masukkan angka yang ingin dicek: '))
print(f'Hasil Fibonacci dari {userInput} : {fiboList(userInput)}')