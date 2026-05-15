# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time

# def myDecorator(func) :  # Decorator

#   def nestedFunc(*n) :# Any Name It's Just For Decoration

#     for i in n :
      
#       if i < 0  :
        
#         print("One Of Two Numbers is Less Than Zero")

#     func(*n) # Execute Function

#   return nestedFunc # Return All Data


# @myDecorator
# def calc(n1, n2, n3, n4) :

#   print(n1 + n2 + n3 - n4)


# calc(10, 20, 30, 22)
# calc(-10, 20, 10, 11)

def speedTest(func) : 

  def wrapper() :

    start = time()

    func()

    end = time()

    print(f"Running Time Is: {end - start}")

  return wrapper

@speedTest
def bigOO() :

  for number in range(1, 10000) :

    print(number)

bigOO()