# --------------------
# -- Function Scope --
# --------------------

# x = 1 # Global Scope

def one() :

  global x

  x = 2

  print(f"Print Var From Function Scope {x}")

def two() :

  x = 10

  print(f"Print Var From Function Scope {x}")

one()
print(f"Print Var From Global Scope {x}")
two()
print(f"Print Var From Global Scope After Calling Fun one() {x}")