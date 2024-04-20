import numpy as np

list_one = [1,2,9]
list_two = [4,5,9]

# convert lists || tuples to nparray
array_1 = np.array((list_one,list_two))

# Create new nparray of zeros
array_2 = np.zeros(5)

# Create new nparray of ones
array_3 = np.ones(5)

# Create new nparray ints form 1 to 9
array_4 = np.arange(1,8 + 1)

# Get Array Dimension Number
# print(array_1.ndim) // 3

# Get Array Data Type 
# print(array_1.dtype) // int32

# Create new shape of one dimension
# print(array_1.reshape(6)) // [1 2 9 4 5 9]

# print(array_1.transpose()) // [[1 4] [2 5] [9 9]]

# Create Copy Of Array
array_1_copy = array_1.copy()
print(array_1_copy)

array_1[0][0] = 10

print(array_1)
print(array_1_copy)


