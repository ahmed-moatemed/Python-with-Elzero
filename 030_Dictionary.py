# --------------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Neet To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Not Ordered You Access It's Element With Key
# --------------------------------

# Dictionary

user = {
  "name" : "Ahmed",
  "age" : 23,
  "country" : "Egypt",
  "skills" : ["Html", "Css", "JS"],
  "rating" : 10.5
}

print(user)
print(user["country"])
print(user.get("country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary

languages = {
  "One" : {
    "name" : "HTML",
    "progress" : "80%"
  },
  "Two" : {
    "name" : "CSS",
    "progress" : "90%"
  },
  "Three" : {
    "name" : "JS",
    "progress" : "90%"
  }
}

print(languages)
print(languages['One'])
print(languages['Three']['progress'])
print(languages['Two']['name'])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
  "name" : "Vuejs",
  "progress" : "80%"
}

frameworkTwo = {
  "name" : "ReactJs",
  "progress" : "80%"
}

frameworkThree = {
  "name" : "Angular",
  "progress" : "80%"
}

allFramework = {
  "one" : frameworkOne,
  "two" : frameworkTwo,
  "three" : frameworkThree
}

print(allFramework)