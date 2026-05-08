# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

# print(1, 2, 3, 4)

# myList = [1, 2, 3, 4]

# print(myList)
# print(*myList)

def sayHello(*peoples) :

  for name in peoples :

    print(f"Hello {name}")

sayHello("Ahmed", "Osama", "Mohamed")
sayHello("Ahmed", "Osama", "Mohamed", "Sayed", "Ali", "Salma")


def show_details(name, *skills) :

  print(f"Hello {name} Your Skills Is: ")

  for skill in skills :

    print(f"- {skill}")


show_details("Ahmed", "HTML", "CSS", "JS")
show_details("Ali", "HTML", "CSS", "JS","Python", "React JS")

