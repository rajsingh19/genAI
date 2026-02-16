import numpy as np

arr = np.array([1,2,3,4,5])

new_arr = np.insert(arr,2,10)  # Insert 10 at index 2
print(new_arr)

new_arr2 = np.insert(arr,2,[8,9]) # Insert 8 and 9 at index 2
print(new_arr2)

arr2 = np.array([[1, 2],
                [3, 4]])

new_arr2 = np.insert(arr2, 1, [5, 6], axis=0)
print(new_arr2)
