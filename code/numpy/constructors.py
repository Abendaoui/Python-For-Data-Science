import numpy as np

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]



array_0 = np.zeros((3,4)) # (3 = Dimension , 4 = size)


arr_empty = np.empty((3,4))

arr_full = np.full((3,4),9)  # (3 = Dimension , 4 = size), 9 = value

arr_random = np.random.randn(5) # array of random numbers

arr_range = np.arange(1,10)

np.append(arr_range,[9,10])

print(arr_range)