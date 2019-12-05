import numpy as np
id, usia = np.loadtxt('numpyExample.csv', skiprows=1, delimiter=",", unpack=1)
print(id)
print(usia)