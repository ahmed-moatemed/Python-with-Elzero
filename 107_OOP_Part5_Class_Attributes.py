# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -------------------------------------------------------


class Member:

    not_allowed_names = ["Hell", "Shit", "Baloot"]

    users_num = 0

    def __init__(self,first_name, midd_name, last_name, gender) :

        self.fname = first_name
        self.mname = midd_name
        self.lname = last_name
        self.gender = gender

        Member.users_num += 1
    
    def full_name(self) :

        if self.fname in Member.not_allowed_names:

            raise ValueError("Name Not Allowed")
        else:

            return f"{self.fname} {self.mname} {self.lname}"        
    
    def name_with_title(self):

        if self.gender == "Male" :

            return f"Hello Mr {self.fname}"
        elif self.gender == "Female" :

            return f"Hello Miss {self.fname}"
        else :

            return f"Hello {self.fname}"
    
    def get_all_info(self):

        return f"{self.name_with_title()}, Your Full Name Is {self.full_name()}"
    
    def delete_user(self) :

        Member.users_num -= 1

        return f"User {self.fname} Deleted."


print(Member.users_num)

member_one = Member("Ahmed", "Ibrahim", "Moatemed", "Male")
member_two = Member("Sara", "Mohamed", "Ali", "Female")
member_three = Member("Osama", "Mohamed", "Elsayed", "Male")

member_four = Member("Shit", "Mohamed", "Elsayed", "Male")

print(Member.users_num)

print(member_four.delete_user())

print(Member.users_num)

# print(f"Member One Is {member_one.fname} {member_one.mname} {member_one.lname}")
# print(member_two.fname, member_two.mname, member_two.lname)
# print(member_three.fname)

# print(member_one.full_name())
# print(member_two.full_name())
# print(member_three.full_name())

# print(member_one.name_with_title())
# print(member_two.name_with_title())

# print(member_one.get_all_info())
# print(member_two.get_all_info())

# print(dir(Member))
