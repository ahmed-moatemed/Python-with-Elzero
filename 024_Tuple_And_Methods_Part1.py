# ------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Can't Add Or Delete
# [5] Tuple Items Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings And Lists Available In Tuples
# ------------------------

# Tuple Syntax & Type Test

myAwesomeTupleOne = ("Ahmed", "Osama")
myAwesomeTupleTwo = "Ahmed", "Osama"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# Tuple Indexing

myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])

# Tuple Assign Values

myAwesomeTupleFour = (1, 2, 3, 4, 5)
myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour) # TypeError: 'tuple' object does not support item assignment

# Tuple Items

myAwesomeTupleFive = ( "Osama", "Ahmed", 1, 2, 3, 100.9, True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])

