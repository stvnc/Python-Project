'''
    x  - 2y +  z =  6
    3x +  y - 2z =  4
    7x - 6y -  z = 10
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

firstEq = np.array([
    [1, -2, 1],
    [3, 1, -2],
    [7, -6, -1]
    ])

valueEquation = np.array([6, 4, 10])

hasil = np.linalg.solve(firstEq, valueEquation)
print(hasil)