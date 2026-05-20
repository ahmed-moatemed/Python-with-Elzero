# -----------------------------------
# --       Exceptions Handling     --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else     => If No Errors
# Finally  => Run The Code
# -------------------------

# number = int(input("Write Your Age: "))

# print(number)
# print(type(number))

# try : # Try Code And Test Errors

#     number = int(input("Write Your Age: "))

# except : # Handle The Errors If It's Found

#     print("Please Enter Number!!")

# else : # If Theres No Errors

#     print("Okay This Is Number")

# finally : # Run Code Whatever Happen

#     print("Print From Finally")


try :

    # print(10/0)
    # print(x)
    print(int("Hello"))

except ZeroDivisionError:

    print("Can't Divide")

except NameError:

    print("Identifier Not Found")

except ValueError:

    print("Value Error M33")

except :

    print("Errors Happens")