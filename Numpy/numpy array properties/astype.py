import numpy as np

# int to float 
arr = np.array([1, 2, 3])
print(arr.dtype)

new_arr = arr.astype(float)
print(new_arr.dtype)

# float to int
arr1 = np.array([1.7, 2.8, 3.9])
new_arr1 = arr1.astype(int)

print(new_arr1)
print(new_arr1.dtype)
