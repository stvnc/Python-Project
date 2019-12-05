angka = [1, 2, 3, 4]
hasil = 1
for i in angka:
    hasil *= i
print(hasil)

from functools import reduce
z = reduce(lambda x, y: x*y, angka)
print(z)

kata = ['Namaku', 'Adalah', 'Vincent']
v = reduce(lambda a, b: a+b, kata)
print(v)

filterList = list(filter(lambda x: x > 3, map(lambda x : x * 2, angka))) # => diproses dari map dulu
print(filterList)

filter2List = list(map(lambda x: x * 2, filter(lambda x: x > 3, angka))) # => diproses dari filter 

angkaBaru = list(range(1,101))
print(reduce(lambda x, y: x + y, map(lambda x: x * 2, filter(lambda a: True if a % 2 == 0 else False, angkaBaru))))
print(list(filter(lambda x: True if x % 7 != 0 or x / 7 == 1 else False, filter(lambda x: True if x % 5 != 0 or x / 5 == 1 else False, filter(lambda x: True if x % 3 != 0 or x / 3 == 1 else False, filter(lambda x: True if x % 2 != 0 or x / 2 == 1 else False, filter(lambda x: True if x != 1 else False, angkaBaru)))))))

def prima(param):
    if param > 1:
        if param == 2:
            a = True
        else:
            for i in range(2, param):
                if param % i == 0:
                    a = False
                    break
                else:
                    a =  True
    else: 
        a =  False
    return a

z = list(filter(prima, angkaBaru))
print(z)