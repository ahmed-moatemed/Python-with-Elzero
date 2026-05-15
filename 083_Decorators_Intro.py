# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometime Called Meta Programming
# [2] Everything in Python is Object Even Function
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# --------------------------------------------------

def myDecorator(func) :  # Decorator

  def nestedFunc() :# Any Name It's Just For Decoration

    print("Before") # Message

    func() # Execute Function

    print("After") # Message

  return nestedFunc # Return All Data

@myDecorator # علشان معملش الي مهمشه تحت
def sayHello() :

  print("Hello........")

@myDecorator
def sayHowAreYou() :

  print("How Are You??")

# afterDecoration = myDecorator(sayHello)

# afterDecoration()

sayHello()

print("#" * 40)

sayHowAreYou()