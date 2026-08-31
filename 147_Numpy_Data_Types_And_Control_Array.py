# -------------------------------------------
# -- Numpy => Data Types And Control Array --
# -------------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types
# -------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating poit
# 'c' complex-floating point
# 'm' timedelta
# 'M' datetime
# 'O' (Pyhton) objects
# 'S', 'a' zero-terminated bytes (not recommended)
# 'U' Unicode string
# 'V' raw data (void)
# -----------------------------------------------

import numpy as np

# Show Array Data Type

my_arr1 = np.array([1, 2, 3])
my_arr2 = np.array([1.5, 20.15, 3.601])
my_arr3 = np.array(["Osa", "B", "Ahmed"])

print(my_arr1.dtype)
print(my_arr2.dtype)
print(my_arr3.dtype)

print("$" * 40)

# Create Array With Specific Data Type

my_arr4 = np.array([1, 2, 3], dtype=float) # float or 'float' or 'f'
my_arr5 = np.array([1.5, 20.15, 3.601], dtype=int) # int or 'int' or 'i'
# my_arr6 = np.array(["Osa", "B", "Ahmed"], dtype=int) # Vaule Error

print(my_arr4.dtype)
print(my_arr5.dtype)
# print(my_arr6.dtype)

print("$" * 40)

# Change Data Type For Existing Array

my_arr7 = np.array([0, 1, 2, 3, 0, 4])
print(my_arr7.dtype)
print(my_arr7)

print("$" * 40)

my_arr7 = my_arr7.astype('float')
print(my_arr7.dtype)
print(my_arr7)

print("$" * 40)

my_arr7 = my_arr7.astype('bool')
print(my_arr7.dtype)
print(my_arr7)

print("$" * 40)

# Test Capacity

my_arr8 = np.array([100, 200, 300, 400], dtype="f")
print(my_arr8.dtype)
print(my_arr8[0].itemsize) # 4 Bytes

my_arr8 = my_arr8.astype('float') # Change to float64
print(my_arr8.dtype)
print(my_arr8[0].itemsize) # 8 Bytes

print("$" * 40)