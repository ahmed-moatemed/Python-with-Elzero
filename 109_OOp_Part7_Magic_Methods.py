# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is an Object
# __init__  Called Automatically When Instanctiating Class
# self.__class__ The Class to Which a Class instance belongs
# __str__  Gives a Human_Readable Output of the Object
# __len__  Returns the Length of The Container 
#          Called When We Use The Built-in len() Function on the Object
# ----------------------------------------------------------

class Skill :

    def __init__(self) :

        self.skills = ["HTML", "CSS", "JS"]
    
    def __str__(self) :

        return f"This is My Skills => {self.skills}"
    
    def __len__(self) :

        return len(self.skills)


profile = Skill()
print(profile)
print(len(profile))


profile.skills.append("PHP")
profile.skills.append("Python")

print(len(profile))


# print(profile.__str__)


# print(profile.__class__)

# my_string = "Ahmed"
# print(type(my_string))
# print(my_string.__class__)
# print(dir(str))
# print(str.upper(my_string))

