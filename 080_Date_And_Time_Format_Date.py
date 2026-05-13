# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# "https://strftime.org/"
# -----------------------

import datetime

myBirthDay = datetime.datetime(2003, 7, 26)

print(myBirthDay)
print(myBirthDay.strftime("%B"))
print(myBirthDay.strftime("%b"))
print(myBirthDay.strftime("%Y"))
print(myBirthDay.strftime("%y"))
print(myBirthDay.strftime("%a"))
print(myBirthDay.strftime("%A"))


print("#" * 40)

print(myBirthDay.strftime("%d %B %Y"))
print(myBirthDay.strftime("%d,%B,%Y"))
print(myBirthDay.strftime("%d/%B/%Y"))
print(myBirthDay.strftime("%d-%B-%Y"))