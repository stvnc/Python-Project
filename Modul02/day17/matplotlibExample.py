import matplotlib.pyplot as plt
import numpy as np
# from matplotlib import pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = x ** 2
z = x ** 3

# plt.plot(x, y, 'y--', x, z, 'b.', y, z, 'k-.') # XY dengan warna red, XZ dengan warna green, YZ dengan warna biru
'''
    ^ = Segitiga,
    s = Square,
    * = Bintang,
    o = Lingkaran besar,
    . = dot,
    .- =  dot garis,
'''

# plt.plot(x, x, 'gs', x, x, 'r:')
plt.plot(x, x, color='r', marker='h', linestyle=':', markersize = 20)

plt.title('Testing')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y/Z')
plt.grid(True)
# plt.legend(['Garis XY', 'Garis XZ', 'Garis YZ'])

plt.savefig('figure.png')
plt.show()