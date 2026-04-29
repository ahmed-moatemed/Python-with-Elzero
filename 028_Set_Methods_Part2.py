# -----------------
# -- Set Methods --
# -----------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "Ahmed", "Ali"}
print(a)
print(a.difference(b)) # a - b
print(a)

print("=" * 40) # Separator

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, 3, "Ahmed", "Ali"}
print(c)
c.difference_update(d) # c - d
print(c)

print("=" * 40) # Separator

# intersection()

e = {1, 2, 3, 4, "X", "Ahmed"}
f = {"Ahmed", "X", 2}
print(e)
print(e.intersection(f))  # e $ f
print(e)

print("=" * 40) # Separator

# intersection_update()

g = {1, 2, 3, 4, "X", "Ahmed"}
h = {"Ahmed", "X", 2}
print(g)
g.intersection_update(h)  # e $ f
print(g)

print("=" * 40) # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"Ahmed", "Zero", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j)) # i ^ j
print(i)

print("=" * 40) # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"Ahmed", "Zero", 1, 2, 4, "X"}
print(k)
k.symmetric_difference_update(l) # i ^ j
print(k)

