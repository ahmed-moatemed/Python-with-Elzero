# --------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# --------------------------

myAwesomList = ["One", "Two", "One", 1, 1000.5, True]

print(myAwesomList) # Whole List 
print(myAwesomList[1]) # "One"
print(myAwesomList[-1]) # True
print(myAwesomList[-3]) # 1

print(myAwesomList[1:4])  # 'Two', 'One', 1
print(myAwesomList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomList[1:]) # ['Two', 'One', 1, 1000.5, True]

print(myAwesomList[::1]) # ['One', 'Two', 'One', 1, 1000.5, True]
print(myAwesomList[::2]) # ['One', 'One', 1000.5]


print(myAwesomList)
# myAwesomList[1] = 2
# myAwesomList[-1] = False
myAwesomList[0:3] = ["A"]
print(myAwesomList)