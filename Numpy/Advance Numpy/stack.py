import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.vstack((arr1, arr2))
print(result)


arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])

result1 = np.hstack((arr3, arr4))
print(result1)
