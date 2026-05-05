# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

# skills = ['Html', 'Css', 'JS']

# for name in peoples : # Outer Loop

#   print(f"{name} Skills Is: ")

#   for skill in skills : # Inner Loop

#     print(f" - {skill}")

peoples = {
  "Osama" : {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed" : {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed" : {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

# print(peoples["Ahmed"])
# print(peoples["Osama"]["Html"])

for name in peoples :

  print(f"Skills and Progress For {name} Is: ")

  for skill in peoples[name] :

    print(f"- {skill.upper()} => {peoples[name][skill]}")