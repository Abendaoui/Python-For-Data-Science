import numpy as np

array_1 = np.full((3,4),8)
array_2 = np.zeros((3,4))

array_3 = np.array([1,2,3])
array_4 = np.arange(1,9)

#  Stack Arrays Horizontaly (axis = 1)
merge_arrays_h = np.hstack((array_1,array_2))

# Stack Arrays Verticaly (axis = 0)
merge_arrays_v = np.vstack((array_1,array_2))

# Concate arrays
concate_array = np.concatenate((array_1,array_2),axis=1)

# Convert 1 dimensional array to 2 dimensional array
array_dim = np.column_stack(array_3)

# Reshape 1 dimensional arrays to  2 dimensional arrays
reshape_array = np.reshape(array_4,(2,4))

# Resize arrays
resized_array = np.resize(reshape_array,(4,2))

# Convert 2 dimensionals array to 1 dimensional array
oned_array = np.ravel((array_1,array_2))

# Shift arra elemet
shift_array = np.roll(array_4,5)

print(shift_array)





