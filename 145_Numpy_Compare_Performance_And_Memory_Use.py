# -------------------------------------------------
# -- Numpy => Compare Performance And Memory Use --
# -------------------------------------------------
# - Performance 
# - Memory Use
# -------------------------------------------------

import numpy as np
import time
import sys

elements = 1500000

my_list1 = range(elements)
my_list2 = range(elements)

my_arr1 = np.arange(elements)
my_arr2 = np.arange(elements)

list_start = time.time()
list_result = [(n1+n2) for n1, n2 in zip(my_list1, my_list2)]
print(f"List Time = {time.time() - list_start}")

arr_start = time.time()
arr_result = my_arr1 + my_arr2
print(f"Numpy Array Time = {time.time() - arr_start}")

print("#" * 40)

my_arr = np.arange(100)

print(my_arr.itemsize)
print(my_arr.size)
print(f"All Bytes = {my_arr.itemsize * my_arr.size}")

print("#" * 40)


my_list = range(100)
print(sys.getsizeof(my_list[0]))
print(len(my_list))
print(f"All Bytes = {sys.getsizeof(my_list[0]) * len(my_list)}")