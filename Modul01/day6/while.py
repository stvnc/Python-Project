'''
students = ['Andi', 'Budi', 'Caca']
index = 0
while(index < len(students)):
    print(students[index])
    index += 1
'''
'''
#Kuadrat - 1st method (while)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
y = []
while index < len(x):
    y.append(x[index]**2)
    index+=1
print(y)
'''
'''
#Kuadrat - 2nd method (function)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []

def powerList(param1, param2):
    for i in param1:
        param2.append(i**2)
    print(param2)

powerList(x, y)
'''

#Password Checker
password = '12345'
status = False
count = 0

if input('Masukkan Password: ') != password:
    while status == False and count < 5:
        userInput = input('Password Salah!, Ketik Password: ')
        if userInput == password:
            status = True
            print('Password Benar!')
        else:
            status = False
            count += 1 
    print('Batas Maksimum Ketik Password Terlampaui, Silahkan Coba Lagi Nanti') 
else:
    print('Password Benar!')





