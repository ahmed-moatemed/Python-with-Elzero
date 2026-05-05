# -----------------
# -- Loop => For --
# -----------------
# For Item in Iterable_object :
#   Do Something With Item 
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# Item refer to the current position and Will run and visit all items to the end 
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# -------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers :

  # print(number * 22)

  if number % 2 == 0 : # Even

    print(f"The Number {number} Is Even.")

  else :

    print(f"The Number {number} Is Odd.")

else :

  print("The Loop Is Finished.")


myName = "Ahmed"

for letter in myName :

  print(f" [ {letter} ] ")