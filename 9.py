import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

#does matrix multiplication
print(np.dot(A,B))

#transpose
print(A.T)

#inverse
print(np.linalg.inv(A))

#determinant
print(np.linalg.det(A))