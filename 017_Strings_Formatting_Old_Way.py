# ------------------------
# -- Strings Formatting --
# ------------------------

name = "Ahmed"
age = 23
rank = 10

print("My Name is: " + name)
#print("My Name is: " + name + " and My Age is: " + age) # Type Error 

print("My Name is: %s" % name)
print("My Name is: %s and My Age: %d" % (name, age))
print("My Name is: %s and My Age: %d and My Rank is: %f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "Ahmed"
l = "Python"
y = 10

print("My Name is: %s I'm %s Developer With %d Years Exp" % (n,l,y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.1f" % myNumber)

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love you All"
print("Message is: %s" % myLongString)
print("Message is: %.5s" % myLongString)