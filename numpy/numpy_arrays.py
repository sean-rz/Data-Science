import numpy as np

my_list = [1,2,3]
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Creating NumPy Arrays
print np.array(my_list)
print np.array(my_matrix)

# Built-in Methods
print np.arange(0,10)
print np.arange(0,11,2)

print np.zeros(3)
print np.zeros((5,5))

print np.ones(3)
print np.ones((3,3))

print np.linspace(0,10,3) # evenly spaced numbers over a specified interval
print np.linspace(0,10,50)

print np.eye(4) # Creates an identity matrix


# Random Numbers
print np.random.rand(2)  # random samples from a uniform distribution over [0, 1)
print np.random.rand(5,5)

print np.random.randn(2)  # samples from the standard normal distribution
print np.random.randn(5,5)

print np.random.randint(1,100) # Return random integers from low (inclusive) to high (exclusive)
print np.random.randint(1,100,10)

# Array Attributes and Methods
arr = np.arange(25)
print arr.reshape(5,5)
print arr.reshape(1,25).shape # (1,25)

ranarr = np.random.randint(0,50,10)
print ranarr.max()
print ranarr.argmax() # return max index

print ranarr.min()
print ranarr.argmin() # return min index

print arr.dtype # data type of dtype('int64')

