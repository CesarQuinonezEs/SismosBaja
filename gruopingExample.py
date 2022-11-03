import numpy as np

A = [0.7, 0.8, 0.4, 0.5, 0.2]
a = np.array((A),dtype=float)
B = [0.6, 0.8, 0.5, 0.4, 0.2]
b = np.array((B), dtype=float)
n = len(A)
sum = 0
for i in range(n):
   sum = sum + ((a[i] - b[i])**2)

r = np.sqrt(sum)

print(sum)