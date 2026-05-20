# ----------------------------------
# -- Errors and Exception Raising --
# ----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Link To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise keyword Used To Raise Your Own Exceptions
# --------------------------------------------------

# x = -10

# if x < 0 :

#     raise Exception(f"The Number {x} Is Less Than Zero")

#     print("Error Can't Make It Print")
# else :

#     print(f"{x} Is Good")

# print("Print Message After If Condition")

y = 11

if type(y) != int :

    raise ValueError("Please Enter Number!?")
else :

    print(f"This Is Number {y}")