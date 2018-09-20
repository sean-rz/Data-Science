import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array(my_list)
d = {'a':10, 'b':20, 'c':30}

print pd.Series(data=my_list)

print pd.Series(data=my_list, index=labels)
print pd.Series(my_list,labels)

print pd.Series(arr)
print pd.Series(arr, labels)

print pd.Series(d) # Dictionary

print pd.Series(data=labels)
# print pd.Series([sum,print,len]) # Even functions

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])

print ser1
print ser2['USA']

print ser1 + ser2