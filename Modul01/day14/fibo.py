class Fibo():
    def __init__(self, range):
        self.range = range

    def fiboList(self):
        fibonacciList = [0,1] # initialnya adalah 0 dan 1 
        for i in range(2, self.range+1):
            fibonacciList.append(fibonacciList[i-2] + fibonacciList[i-1])
            print(fibonacciList[i])
        return fibonacciList[self.range]

userInput = int(input('Masukkan angka yang ingin dicek: '))
fibo = Fibo(userInput)

print(f'Hasil Fibonacci dari {userInput} : {fibo.fiboList()}')