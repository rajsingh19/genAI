import numpy as np

# Given array
values = np.array([2, 4, 6, 8, 10])

# 1. Square root of each element
square_root = np.sqrt(values)

# 2. Exponential of each element
exponential = np.exp(values)

# 3. Natural logarithm of each element
natural_log = np.log(values)

# 4. Sum of all elements
total_sum = np.sum(values)

# 5. Cumulative sum of elements
cumulative_sum = np.cumsum(values)

#  results
print("Original Array:", values)
print("Square Root:", square_root)
print("Exponential:", exponential)
print("Natural Logarithm:", natural_log)
print("Sum of Elements:", total_sum)
print("Cumulative Sum:", cumulative_sum)
