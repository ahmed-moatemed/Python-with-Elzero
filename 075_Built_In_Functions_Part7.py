# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate() 
# help() 
# reversed() 
# -----------------------

# enumerate(iterable, start = 0)

mySkills = ["Html", "Css", "JS", "PHP"]

mySkillsWithCounter = enumerate(mySkills, start=10)

print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter : 
  
  print(f"{counter} - {skill}")

print("#" * 40)

# help()  help you to know any thing in lang

# print(help(print))

print("#" * 40)

# reversed(iterable)

myString = "Ahmed"
print(reversed(myString))

for l in reversed(myString) :

  print(l)

print("#" * 40)

myString = "Ahmed"
print(reversed(mySkills))

for s in reversed(mySkills) :

  print(s)