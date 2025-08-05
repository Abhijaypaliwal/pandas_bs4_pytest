import numpy as np
arr = np.array([1,2,3,4,5])


multi_dimension = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(multi_dimension[1:3])
print(multi_dimension[:,1]) #print 2,5,8

#boolean indexing
mask = arr > 3
print(arr[mask]) #prints elements greater than 3, which is 4 and 5

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)   # [11 22 33]
print(a - b)   # [-9 -18 -27]
print(a * b)   # [10 40 90]
print(b / a)   # [10. 10. 10.]

arr = np.array([1, 3, 5, 7, 9])

print(np.sum(arr))     # 25
print(np.mean(arr))    # 5.0
print(np.std(arr))     # 2.828...
print(np.min(arr))     # 1
print(np.argmax(arr))  # 4 (index of 9)

#can multiply 1D array to 2d array
a = np.array([[1, 2, 3], [4,5,6]])
b = np.array([10, 20, 30])
print(np.mean(a+b))



