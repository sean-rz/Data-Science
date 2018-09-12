import numpy as np

arr = np.arange(0,11)
print arr[1:5]

arr[0:5] = 100  # broadcasting
print arr

arr = np.arange(0,11)
slice_of_arr = arr[0:6]
slice_of_arr[:]=99
print slice_of_arr

arr_copy = arr.copy()
print arr_copy

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print arr_2d

print arr_2d[1] #Indexing row
print arr_2d[1][0]
print arr_2d[1,0] # Format is arr_2d[row][col] or arr_2d[row,col]
print arr_2d[:2,1:] # 2D array slicing
print arr_2d[2,:]

arr2d = np.zeros((10,10))
arr_length = arr2d.shape[1] #Length of array

#Set up array
for i in range(arr_length):
    arr2d[i] = i

print arr2d[[2,4,6,8]]
print arr2d[[6,4,2,7]]

# Selection
arr = np.arange(1,11)
bool_arr = arr > 4
print arr[bool_arr]

x = 2
print arr[arr > 2]
print arr[arr > x]
