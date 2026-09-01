# ---------------------------------------------
# -- Numpy => Arithmetic & Useful Operations --
# ---------------------------------------------
# - Additon
# - Subtraction
# - Multiplication
# - Dividation
# ----------------
# - min
# - max
# - sum
# - ravel => Returns Flattened Array 1 Dimension With Same Type
# ----------------------------------------------

import numpy as np

# Arithmetic  Operations

my_arr1 = np.array([10, 20, 30])
my_arr2 = np.array([5, 2, 4])

print(my_arr1 + my_arr2) # result [15, 22, 34]
print(my_arr1 - my_arr2) # result [5, 18, 26]
print(my_arr1 * my_arr2) # result [50, 40, 120]
print(my_arr1 / my_arr2) # result [2, 10, 7.5]

print("$" * 40)

my_arr3 = np.array([[1, 4], [5, 9]])
my_arr4 = np.array([[2, 7], [10, 5]])

print(my_arr3 + my_arr4) # result [ [3, 11], [15, 14] ]
print(my_arr3 - my_arr4) # result [ [-1, -3], [-5, 4] ]
print(my_arr3 * my_arr4) # result [ [2, 28], [50, 45] ]
print(my_arr3 / my_arr4) # result [ [0.5, 0.57142857], [0.5, 1.8]]

print("$" * 40)

# Min, Max, Sum

my_arr5 = np.array([10, 20, 30])
print(my_arr5.min())
print(my_arr5.max())
print(my_arr5.sum())

print("$" * 40)

my_arr6 = np.array([[6, 4], [3, 9]])
print(my_arr6.min())
print(my_arr6.max())
print(my_arr6.sum())

print("$" * 40)

# Ravel

my_arr7 = np.array([[6, 4], [3, 9]])
print(my_arr7.ravel())

my_arr8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(my_arr8.ndim)
print(my_arr8.ravel())
x = my_arr8.ravel()
print(x.ndim)