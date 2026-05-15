# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def myDecorator(func) :  # Decorator

  def nestedFunc(a, b) :# Any Name It's Just For Decoration

    if a < 0 or b < 0 :

      print("One Of Two Numbers is Less Than Zero")

    func(a, b) # Execute Function

    # print("After") # Message

  return nestedFunc # Return All Data


def myDecoratorTwo(func) :  # Decorator

  def nestedFunc(a, b) :# Any Name It's Just For Decoration

    print("Come From Decorator Two")

    func(a, b) # Execute Function

  return nestedFunc # Return All Data

@myDecorator
@myDecoratorTwo
def calc(n1, n2) :

  print(n1 + n2)


calc(10, 20)

print("#" * 40)

calc(-20, 40)