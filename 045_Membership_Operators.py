# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String 

name = "Ahmed"
print("e" in name)
print("A" in name)
print("a" in name)

print("#" * 50)

# List 

frinds = ["Ahmed", "Mohamed", "Ali"]
print("Sayed" in frinds)
print("Ali" in frinds)
print("Mohamed" not in frinds)

print("#" * 50)

# Using In and Not In With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Egypt"

if myCountry in countriesOne :

  print(f"Hello You Have A Discount Equal => ${countriesOneDiscount}")

elif myCountry in countriesTwo :

  print(f"Hello You Have A Discount Equal => ${countriesTwoDiscount}")

else:

  print("You Have No Discount")