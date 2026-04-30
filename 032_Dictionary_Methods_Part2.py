# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
  "name" : "Ahmed"
}
print(user)
print(user.setdefault("age" , 23))
print(user)

print("=" * 50)

# popitem()

member = {
  "name" : "Ahmed",
  "skill" : "PS4"
}
print(member)
member.update({"age" : 23})
print(member.popitem())

print("=" * 50)

# items()

view = {
  "name" : "Ahmed",
  "skill" : "XBox"
}

allItems = view.items()
print(view)
view["age"] = 23

print(allItems)

print("=" * 50)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))

