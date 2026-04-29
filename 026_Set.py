# ----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing And Slicing Can't Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List And Dict Are Not
# [5] Set Items Is Unique
# ----------------------------

# Not Ordered And Not Indexed

mySetOne = {"Ahmed", "Ali", 100}
print(mySetOne)
# print(mySetOne[0]) # Error

# Slicing Can't Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3]) # Error

# Has Only Immutable Data Types

# mySetThree = { "Ahmed", 100.5, 100, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = { "Ahmed", 100.5, 100, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "Ahmed", "One", "Ahmed", 1}
print(mySetFour)