# ----------------------------
# -- Numpy => Create Arrays --
# ----------------------------

import numpy as np

# print(dir(np))

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("#" * 40)

# Type

print(type(my_list))
print(type(my_array))

print("#" * 40)

# Accessing Elements

print(my_list[0])
print(my_array[0])

print("#" * 40)

a = np.array(10)
b = np.array([10, 20])
c = np.array([[1, 2], [3, 4]])
d = np.array([ [ [11, 12], [13, 14] ], [ [15, 16], [17, 18] ] ])

print(d[1][1][1])
print(d[1, 1, 1])
print(d[1, 1, -1])

print("#" * 40)

# Numper of Dimensions

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("#" * 40)

# Custom Dimensioins

my_custom_array = np.array([1, 2, 3], ndmin=3)

print(my_custom_array)
print(my_custom_array.ndim)
print(my_custom_array[0, 0, 2])