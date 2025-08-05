import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(pd.__version__)

data =  pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, np.nan,"hello"])



data1 = pd.Series([10,20,30], index=['a','b','c'])

print(data1['a'])