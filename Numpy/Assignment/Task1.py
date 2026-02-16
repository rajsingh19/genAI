import numpy as np
list = [10,20,30,40,50]
arr_1d = np.array([1,2,3,4,5,6,7,8,9,10])

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
arr = np.array(list)

print(np.shape(arr_1d))
print(np.shape(arr_2d))
print(np.shape(arr))

print(arr_1d.dtype)
print(arr_2d.dtype)
print(arr.dtype)