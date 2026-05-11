# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function Or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------

# EXample 1

def checkNumber(n) :
                    # n == 0

    return n > 10  # return True    (to print 0)
  
myNumbers = [1, 19, 10, 20, 100, 5]

myResult = filter(checkNumber, myNumbers)

for number in myResult :

  print(number)

print("#" * 40)

# EXample 2

def checkName(name) :

  return name.startswith("O")
  
myTexts = ["Ahmed", "Osama", "Ola", "Omar", "Ali"]

myReturnData = filter(checkName, myTexts)

for name in myReturnData :

  print(name)

print("#" * 40)

# EXample 3

myNames = ["Ahmed", "Osama", "Ola", "Omar", "Ali"]

# myReturnNames = filter(lambda name : name.startswith("A"), myNames)

for name in filter(lambda name : name.startswith("A"), myNames) :

  print(name)