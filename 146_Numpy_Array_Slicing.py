# ----------------------------
# -- Numpy => Array Slicing --
# ----------------------------

import numpy as np

# Slicing => [Start:End:Steps] not Including End

a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim)
print(a[0])
print(a[1:4:1])
print(a[:4])
print(a[2:])

print("#" * 40)

b = np.array([["A", "B", "X"], ["C", "D", "Y"], ["E", "F", "Z"], ["M", "N", "O"]])

print(b.ndim)
print(b[0])
print("#" * 40)
print(b[:3, :2])

print("#" * 40)
print(b[2:, :2])

print("#" * 40)
print(b[2:, ::2])