# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date and Time
print(datetime.datetime.now())

print("#" * 50)

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#" * 50)

# Print Start And End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 50)

# print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("#" * 50)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("#" * 50)

# Print Start And End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("#" * 50)

# Print Specific Date
print(datetime.datetime(1965, 4, 30))
print(datetime.datetime(1965, 4, 30, 5, 20, 30))

print("#" * 50)

myBirthDay = datetime.datetime(1965, 4, 30)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And", end=" ")
print(f"Date Now is {dateNow}")

print(f"I Lived For {dateNow - myBirthDay}")
print(f"I Lived For {(dateNow - myBirthDay).days} Days.")
print(f"I Lived For {((dateNow - myBirthDay).days)/365.25:.0f} Years.")