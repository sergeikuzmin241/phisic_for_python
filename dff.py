# Дискретная разность

import numpy as np

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)  # [5 10 -20]

arr1 = np.array([10, 15, 25, 5])
newarr1 = np.diff(arr1, n=2)
print(newarr1)  # [ 5 -30]