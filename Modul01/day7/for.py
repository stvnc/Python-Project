'''
for i in range(2, 10, 2): #-> param 1 : mulainya, param2 : end-nya, param3: interval
    print(i)
# print('OK')

for i in range(1, 11):
    if i%2==0:
        print('WOW')
    else:
        print(i)
'''
''' 
#For Method
for i in range(1,16):
    if i%(3*5)==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0:
        print('Fizz')
    else:
        print(i)
'''
'''
#Function Method
def fizzBuzzChecker(param):
    fizz = 3
    buzz = 5
    for i in range(1, param+1):
        if i % fizz == 0 and i % buzz == 0:
            print('FizzBuzz')
        elif i % fizz == 0:
            print('Fizz')
        elif i % buzz == 0:
            print('Buzz')
        else:
            print(i)

fizzBuzzChecker(int(input('Masukkan angka yang diinginkan: ')))
'''
'''
#Reversed method
x = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(reversed(x)))
'''
x = [3, 1, 2, 5, 7, 8, 4, 6]

#Temporary method
def reverseList(param):
    temp = 0
    final = len(param)-1
    if len(param)%2==1:
        for i in range(0, int(len(param)/2)+1):
            temp = param[i]
            param[i] = param[final]
            param[final] = temp
            final-=1
        print(param)
    else:
        for i in range(0, int(len(param)/2)):
            temp = param[i]
            param[i] = param[final]
            param[final] = temp
            final -= 1
        print(param)
reverseList(x)

#Insert Method
def balikPosisiInsert(myList):
    hasil = []
    for i in range(len(myList)):
        hasil.insert(0, myList[i])
    return hasil

print(balikPosisiInsert(x))

#Indexing Method
def balikPosisiIndex(myList):
    for i in range(round(len(myList)/2)):
        temp = myList[i]
        myList[i] = myList[len(myList)-1-i]
        myList[len(myList)-1-i] = temp
    return myList

balikPosisiIndex(x)
            
