# 1️⃣ Arithmetic Operations
import numpy as np
'''
arr = np.array([10, 20, 30])

print(arr + 5)     # Addition
print(arr - 5)     # Subtraction
print(arr * 2)     # Multiplication
print(arr / 2)     # Division
print(arr // 3)    # Floor division
print(arr % 3)     # Modulus
print(arr ** 2)    # Power
'''
# 2️⃣ Array-to-Array Operations
'''
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
'''
# 3️⃣ Comparison Operations
'''
arr = np.array([10, 20, 30])

print(arr > 15)
print(arr < 25)
print(arr == 20)
print(arr != 10)

'''
# 4️⃣ Logical Operations
'''
a = np.array([True, False, True])
b = np.array([False, False, True])

print(np.logical_and(a, b))
print(np.logical_or(a, b))
print(np.logical_not(a))

'''
# 5️⃣ Statistical Operations
'''
arr = np.array([10, 20, 30])

print(arr.sum())
print(arr.mean())
print(arr.min())
print(arr.max())
print(arr.std()) # for finding standard deviation
print(arr.var()) # for finding variance

'''
# 6️⃣ Aggregation Operations
'''
arr = np.array([10, 20, 30])

print(np.sum(arr))
print(np.cumsum(arr))
print(np.prod(arr))

'''
# 7️⃣ Matrix Operations (2D Arrays)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a + b)
print(a @ b)        # Matrix multiplication
print(np.dot(a, b))
print(a.T)          # Transpose

