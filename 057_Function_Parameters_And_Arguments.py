# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a, b, c = "Ahmed", "Osama", "Sayed"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")


# def                       => Function Keyword [Define]
# sayHello()                => Function Name
# name                      => Parameter
# print(f"Hello {name}")    => Task
# sayHello("Ahmed")         => Ahmed is The Argument

def sayHello(name) :

  print(f"Hello {name}")

sayHello(a)
sayHello(b)
sayHello(c)


def addition(x1, x2) :

  print(x1 + x2)


addition(10, 20)
addition(-110, 200)

def addition(x1, x2) :

  if type(x1) != int or type(x2) != int :

    print("Only Integers Allowed")

  else :

    print(x1 + x2)

addition(10, 100)

def full_name(f, m, l) :

  print(f"Hello {f.strip().capitalize()} {m.upper():.1s} {l.capitalize()}")

full_name("Ahmed", "Ibrahim", "Moatemed")