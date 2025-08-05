import time
import numpy as np

single = np.array([1,2,3,4,5,7.6, "helo"])

print(single)

multi_dimension = np.array([[1,2,3],[4,5,6]])

print(multi_dimension)
#create 4 rows and 3 columns with zeros in it
demo =np.zeros((3,4))
print(demo)
#create 4 rows and 3 columns with ones in it
demo1 = np.ones((3,4))
print(demo1)
#make array with 2 difference
demo2 = np.arange(0,10,2)
print(demo2)
# only 2 values should be printed as 2 values are given tio print, else behaves as dividing
# equally
demo3 = np.linspace(0,10,2)
print(demo3)

demo4 = np.eye(3)
print(demo4)
# 2x2 matrix and give random values between 0 and 1
demo5 = np.random.rand(2,2)
print(demo5)

#numpy array attributes
# .shape(), .size(), .type(), .dimension()

print("shape",multi_dimension.shape)
print("dimensions",multi_dimension.ndim)
print("size",multi_dimension.size)
print("data type",multi_dimension.dtype)