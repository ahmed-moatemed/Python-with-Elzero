# ------------------------
# -- Function => Lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used Fro simple Function and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# --------------------------------------------------

def say_hello(name, age) : return f"Hello {name} Your Age is: {age}"

hello = lambda name, age : f"Hello {name} Your Age is: {age}"

print(say_hello("Ahmed",23))
print(hello("Ahmed",23))

print(say_hello.__name__)
print(hello.__name__)

print(type(say_hello))
print(type(hello))