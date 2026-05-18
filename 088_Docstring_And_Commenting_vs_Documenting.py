# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] There's One Line and Multiple Line Doc Strings
# --------------------------------------------------

def ahmed_Func(name) :
  # '''This is Function To Say Hello From Ahmed''' # To make One Line From Doc

  """
  Ahmed Function 
    It Is Func To Say Hello
  Parameter:
    name => Person Name That Use Function 
  Return:
    Return Hello Name Of Person
  """ # To make Multiple Line 
  print(f"Hello {name} From Ahmed")


ahmed_Func("Osama")

# print(dir(ahmed_Func))
# print(ahmed_Func.__doc__)
# help(ahmed_Func)