# ------------------------------------
# -- Numpy => Array Shape & ReShape --
# ------------------------------------
# Shape Returns A Tuple Contains The Number Of Elements in Each Dimension
# ----------------------------------------------

import numpy as np

my_arr1 = np.array([1, 2, 3, 4])
print(my_arr1.ndim)
print(my_arr1.shape)

print("$" * 40)

my_arr2 =np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]) # 3 plue 4 in plue
# print(my_arr2)
print(my_arr2.ndim)
print(my_arr2.shape)

print("$" * 40)

my_arr3 =np.array([[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]]) # 2 plue 2 yellow 5 in yellow
# print(my_arr3)
print(my_arr3.ndim)
print(my_arr3.shape)

print("$" * 40)

my_arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(my_arr4.ndim)
print(my_arr4.shape)

reshape_arr4 = my_arr4.reshape(2, 6)
print(reshape_arr4.ndim)
print(reshape_arr4.shape)
print(reshape_arr4)

reshape_arr4 = my_arr4.reshape(3, 4)
print(reshape_arr4.ndim)
print(reshape_arr4.shape)
print(reshape_arr4)

print("$" * 40)

my_arr5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(my_arr5.ndim)
print(my_arr5.shape)

print("$" * 40)

reshape_arr5 = my_arr5.reshape(-1)
print(reshape_arr5.ndim)
print(reshape_arr5.shape)
print(reshape_arr5)

print("$" * 40)

reshape_arr5 = my_arr5.reshape(5, 4)
print(reshape_arr5.ndim)
print(reshape_arr5.shape)
print(reshape_arr5)

print("$" * 40)

reshape_arr5 = my_arr5.reshape(4, 5)
print(reshape_arr5.ndim)
print(reshape_arr5.shape)
print(reshape_arr5)

print("$" * 40)

reshape_arr5 = my_arr5.reshape(2, 5, 2)
print(reshape_arr5.ndim)
print(reshape_arr5.shape)
print(reshape_arr5)

print("$" * 40)

reshape_arr5 = my_arr5.reshape(2, 2, 5)
print(reshape_arr5.ndim)
print(reshape_arr5.shape)
print(reshape_arr5)