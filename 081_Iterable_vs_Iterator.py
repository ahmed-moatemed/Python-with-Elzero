# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ----------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# ---------------------------------------------------

myString = "Ahmed"

myList = [1, 2, 3, 4, 5]

myNumber = 10   # int, float, boolean Not Iterable

# for letter in myString :

#   print(letter, end=" ")

# for n in myList :

#   print(n, end=" ")

# myIterator = iter(myString)

# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))


for letter in "Mo3temed" :

  print(letter, end=" ")