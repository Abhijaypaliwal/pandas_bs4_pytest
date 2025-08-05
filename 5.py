import time
import numpy as np

# py_list = list(range(1,100000000))
# start = time.time()
# py_list = [ x**2 for x in py_list ]
# print("by normal array",time.time()-start)

np_array = np.arange(1,100000000)
start = time.time()
np_array = np_array ** 2
print("by numpy array",time.time()-start)