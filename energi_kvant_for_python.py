# Коментарии для Юпитера

# Первая строка
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.linalg import eigh_tridiagonal

# Вторая строка
N = 2000
dy = 1/N
y = np.linspace(0, 1, N+1)
# print(y)

# 3-я строка
def mL2V(y):
    return 1000*(y-1/2)**2

# 4-я строка
V = mL2V(y)

# 5-я строка
plt.plot(y, V)
# plt.show()

# 6-я строка
d = 1/dy**2 + mL2V(y)[1:-1]
e = -1/(2*dy**2) * np.ones(len(d)-1)
# print(d)
# print(e)

# 7-я строка
w, v = eigh_tridiagonal(d, e)

# 8-я строка
plt.plot(v.T[0]**2)
plt.plot(v.T[1]**2)
plt.plot(v.T[2]**2)
plt.plot(v.T[3]**2)
plt.show()
# 9-я строка
plt.bar(np.arange(0, 10, 1), w[0:10])
plt.ylabel('$ml^2 E/\hbar^2$')
plt.show()