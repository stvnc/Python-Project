import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([[1,2,3],[4,5,6]])
z = np.array([[[1,2,3],[4,5,6],[7,8,9]]]) 

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
print(np.random.rand(2,4))
print(np.random.randint(10, size=(2,5))) #2 dimensi, masing2 dimensi memiliki 5 elemen

#spacing
print(np.linspace(0, 100, 5)) #jarak dari 1 sampai 100 dengan total 5 elemen

a = np.array([(1,2,3,4,5), (4,5,6,7,8), (7,8,9,10,11)])
print(a[0,2])
print(a[0:,:1].reshape(3)) #3 elemen, 1 dimensi

a = np.array([
    [0,-7],
    [-1,3]
])

b = np.array([
    [2,4],
    [3,8]
])

print(a+b)
print()
print(a-b)
print()
print(a+2)


# print(type(y))
# print(y.ndim)
# print(z.ndim)
