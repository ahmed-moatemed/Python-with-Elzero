# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Ahmed", "Ali", "Mohamed"]
myOldFriend = ["Mahmoude", "Sayed", "Sa3d"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriend)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()

a = [1 , 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# removd()

x = [1, 2, 3, 4, 5, "Ahmed", True, "Ahmed", "Ahmed"]
x.remove("Ahmed") 
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "Ahmed", 100]
z.reverse()
print(z)