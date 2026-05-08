# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

# def show_skills(*skills) :

#   print(type(skills))

#   for skill in skills :

#     print(f"- {skill}")

# show_skills("C++", "Pyhton", "JS")

mySkills = {
  "C++": "70%",
  "Python" : "80%",
  "JS" : "60%",
  "CSS" : "75%"
}

def show_skills(**skills) :

  print(type(skills))

  for skill, value in skills.items() :

    print(f"- {skill} => {value}")

# show_skills(C = "70%", Python = "80%", JS = "60%")
show_skills(**mySkills)