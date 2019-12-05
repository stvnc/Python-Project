import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([[1, 2, 3], [4, 5, 6]])
z = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]) 

print(x)
print(x.size)
print(y)
print(y.size)
print(z.astype('float64'))
print(z.size)
print(z.dtype)
print(z.itemsize)
print(z.shape)

print(np.arange(10))
print(np.random.rand(2, 4))
print(np.random.randint(10, size=(2,5))) #2 dimensi, masing2 dimensi memiliki 5 elemen

#spacing
print(np.linspace(0, 100, 5)) #jarak dari 1 sampai 100 dengan total 5 elemen

a = np.array([(1, 2, 3, 4, 5), (4, 5, 6, 7, 8), (7, 8, 9, 10, 11)])
print(a[0, 2])
print(a[0:, :1].reshape(3)) #3 elemen, 1 dimensi

a = np.array([
    [0, -7],
    [-1, 3]
])

b = np.array([
    [2, 4],
    [3, 8]
])

print(a+b)
print()
print(a-b)
print()
print(a+2)

a = np.array([
    [2, 1], [1, 1]
])
b = np.array([5, 7])

hasil = np.linalg.solve(a,b)
print(hasil)

#4x + 7y = 2
#3x - 2y = -5

a = np.array([
    [4, 7],
    [3, 2]
])

b = np.array(
    [2, -5]
)

hasil = np.linalg.solve(a,b)

#2x - 3y = ?
print(f'2x - 3y = {int(2*hasil[0] - 3*hasil[1])}')

# ayam, kambing = 25 ekor
# jumlah kaki 70
#x + y = 25
# 2x + 4y = 70

a = np.array([
    [1, 1],
    [2, 4]
])

b = np.array(
    [25, 70])

hasil = np.linalg.solve(a,b)

print(f'Ayam = {int(hasil[0])}, Kambing = {int(hasil[1])}')

#2x + y + z = 4700
#x + 2y + z = 4300
#3x + 2y + z = 7100

a = np.array([
    [2, 1, 1],
    [1, 2, 1],
    [3, 2, 1]])

b = np.array(
    [4700, 4300, 7100]
)

hasil = np.linalg.solve(a,b)

import math

print(f'Buku tulis = {int(hasil[0])}, Pensil = {math.ceil(hasil[1])}, Penghapus = {int(hasil[2])}')
# print(type(y))
# print(y.ndim)
# print(z.ndim)
print ('Max Min Lambda')

from functools import reduce
x = [[1, 20, 3, 400, 5], [3, 5, 7, 9, 11]]
xsum = reduce(lambda a,b: a+b, x)
xmax = reduce(lambda a,b: a if a > b else b, x)
xmin = reduce(lambda a,b: a if a < b else b, x)
print(xsum)
print(xmax)
print(xmin)

print('Max Min Numpy')

y = np.array(x)
print(y.max())
print(y.min())
print(np.argmax(y))
print(np.argmin(y))

print('Shape')
print(y.shape)
print(y.reshape(10))
print(y.reshape(-1)) #
print(y.reshape(-1, 1, 2)) #terserah berapa banyak dimensi, masing-masing dimensi memiliki 2 elemen

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[0, 0, 0], [0, 0, 0]])
print(b.dtype)
c = np.zeros((2, 3), dtype='int32')
print(c.dtype)
print(c)

a = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
d = np.ones((3, 3), dtype='int32')
print(d)

x = np.zeros((3, 3), dtype=bool)
print(x)

x = np.ones((3, 3), dtype=bool)
print(x)

lain = np.full((3, 3), 1)
print(lain)

lain = lain.tolist()
print(type(lain))

#Cara 1
x = [0, 1, 2, 3, 4]
y = [5, 6, 7, 8, 9]
z = []
z.append(x)
z.append(y)
print(z)

#Cara 2
z = [x, y]
print(z)

#Cara 3
z = np.array(x + y).reshape(2, -1).tolist()
print(z)

#Cara 4

#Cara 5
xnp = np.array(x)
ynp = np.array(y)
z = np.concatenate([[xnp], [ynp]], axis=0).tolist()
print(z)

#Cara 6
z = np.vstack([xnp, ynp]).tolist()
print(z)

#Cara 7
z = np.r_[[xnp], [ynp]].tolist()
print(z)

#Cara 8
z = np.row_stack((xnp, ynp)).tolist()
print(z)

#Cara 9

z = np.arange(1, 11)
print(z)
print(z[1::2])
print(z[z % 2 == 0])

x = np.arange(10, 20)
print(x[np.where(x < 6)])
print(x[np.where((x > 14) & (x < 18))])
print(x[np.where(np.logical_and(x > 14, x < 18))])
print(x[(x > 14) & (x < 18)])

x = np.array([[3, 1], [5, 2]])

print(np.linalg.det(x))

y = np.array([[1, 2, 1], [3, 3, 1], [2, 1, 2]])
print(y)
print(np.linalg.det(y))

z = np.array([[3, 2], [1, 4]])
print(np.linalg.inv(z))

a = np.array([1, 2, 3])
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])