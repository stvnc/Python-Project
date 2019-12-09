'''
print("Print full Triangle pyramid using stars ")
size = int(input('Masukkan angka yang diinginkan: '))
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("*", end=' ')
    print(" ")
'''
cap = 1
for bil in range(1, 20, 2):
    print(cap * " " + (20 - bil) * "* " + bil * " ")
    cap += 2

cap = 1
for bil in range(1, 20, 2):
    print((20 - cap)* " " + bil * "* ")
    cap += 2