#SVD

import numpy as np
import math

M = np.array([[3,2], [2,3], [2,-2]])
A = M.T@M
E,S = np.linalg.eig(A)
print("\nV.T: ")
print(S.T)

a = M@M.T
e,b = np.linalg.eig(a)
print("\nU; ")
print(b)

size = M.shape
s = np.zeros(size)
for i in range(size[1]):
    s[i][i] = np.sqrt(E[i])
print("\nSigma matrix is: ")
print(s)

m = b @ s @ S.T
print("\nThe matrix is: ")
print(m)
