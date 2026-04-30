# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
  "name" : "Ahmed"
}

print(user)
user.clear()
print(user)

print("=" * 50)

# update()
member = {
  "name" : "Ahmed"
}
print(member)
member["age"] = 23
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# copy()

main = {
  "anme" : "Ahmed"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

print("=" * 50)

# keys() + values()

print(main.keys())
print(main.values())