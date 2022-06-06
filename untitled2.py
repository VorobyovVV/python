import numpy as np
a = np.arange(10)
b = a[2:6]
print(a, b)
b[:] = np.arange(30, 34)
print(a, b)


x, y = np.mgrid[range(0, 3), 0:5]
print(x, y)

r = np.random.rand(5, 5)
print(np.diag(range(0, 5), 0))
print(np.diag(range(0, 4), 1))

print(r)
np.diag(np.diag(r, 3), 1)
