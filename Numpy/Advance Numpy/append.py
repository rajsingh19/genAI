import numpy as np

arr = np.array([10, 20, 30])

new_arr = np.append(arr, 40)
print(new_arr)

arr1 = np.array([[1, 2],
                [3, 4]])

new_arr1 = np.append(arr1, [[5, 6]], axis=0)
print(new_arr1)
