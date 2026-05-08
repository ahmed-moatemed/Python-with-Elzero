# ----------------------------------
# -- Function Default Parameteres --
# ----------------------------------

def say_hello(name = "Unknown", age = "Unknown", country = "Unknown") :

  print(f"Hello {name} Your Age is {age} and Your Country is {country}")

say_hello("Ahmed", 23, "Egypt")
say_hello("Ali", 26, "Egypt")
say_hello("Ahmed", 22)
say_hello("Osama")
say_hello()