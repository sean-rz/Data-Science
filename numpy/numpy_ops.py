import numpy as np

arr = np.arange(0,10)

print arr + arr
print arr - arr
print arr * arr
print arr / arr # Warning on division by zero, but not an error!
print 1 / arr
print arr ** 3
print arr * 5
print arr - 100

#  Universal Array Functions
# https://docs.scipy.org/doc/numpy/reference/ufuncs.html

print np.sqrt(arr)
print np.exp(arr)  # #Calcualting exponential (e^)
print np.max(arr)
print np.sin(arr)
print np.log(arr)
