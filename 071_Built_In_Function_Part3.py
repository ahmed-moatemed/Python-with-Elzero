# -----------------------
# -- Built In Function --
# -----------------------
# abs() 
# pow() 
# min() 
# max() 
# slice() 
# -----------------------

# abs()
print(abs(10))
print(abs(-10))
print(abs(12.22))
print(abs(-12.22))

print("#" * 40)

# pow(base, exp, mod) => Power
print(pow(2, 4)) # 2 * 2 * 2 * 2
print(pow(2, 4, 11)) # (2 * 2 * 2 * 2) % 11

print("#" * 40)

# min(item, item, item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -20, 33))
print(min("A", "X", "W", "Ahmed"))
print(min(myNumbers))

print("#" * 40)

# max(item, item, item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -20, 33))
print(max("A", "X", "W", "Ahmed"))
print(max(myNumbers))

print("#" * 40)

# slice(start, end, step)
a = ["A", "B", "C", "D", "E", "F"]
print(a[:4])
print(a[slice(4)])
print(a[slice(2, 5)])
print(a[slice(0, 5, 2)])