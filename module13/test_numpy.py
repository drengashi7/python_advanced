from array import array

import numpy as np

array2d = np.array([[1,2,3,4,5], [6,7,8,9,0]])
print(array2d)

element = array2d[0,4]
print(element)

element1 = array2d[1,2]
print(element1)

array_d = array2d.ndim
print(array_d)

arr_shape = array2d.shape
print(arr_shape)

arr_size = array2d.size
print(arr_size)