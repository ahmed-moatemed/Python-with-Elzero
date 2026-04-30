# -----------------------
# -- Boolean Operators --
# -----------------------
# and 
# or 
# not
# -----------------------

age  = 23
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 1) # True
print(age > 16 and country == "KSA" and rank > 1) # False

print(age > 30 or country == "KSA" or rank > 20) # False
print(age > 30 or country == "Egypt" or rank > 20) # True

print(age > 16) # True
print(not age > 16) # Not True = False