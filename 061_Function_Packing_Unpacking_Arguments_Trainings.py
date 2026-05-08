# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

myTuple = ("HTML", "CSS", "JS")

mySkills = {
  'GO': '80%',
  'JAVA': '85%',
  'Python': '60%',
  'MySQL': '70%'
}

def show_skills(name, *skills, **skillsWithProgres) : 

  print(f"Hello {name} \nSkills Without Progress Is : ")

  for skill in skills:

    print(f"- {skill}")

  print("Skills With Progress Is: ")

  for skill_key, skill_value in skillsWithProgres.items() :

    print(f"- {skill_key} => {skill_value}")


show_skills("Ahmed", *myTuple, **mySkills)