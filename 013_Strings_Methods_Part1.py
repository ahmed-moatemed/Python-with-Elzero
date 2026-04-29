# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()
a = "      I Love Python     "
print(a.strip()) # both
print(a.rstrip()) # from right
print(a.lstrip()) # from left

a = "######I Love Python######"
print(a.strip("#")) # both
print(a.rstrip("#")) # from right
print(a.lstrip("#")) # from left

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#")) # both
print(a.rstrip("@#")) # from right
print(a.lstrip("@#")) # from left

# title()

b = "I Love 2d Graphics and 3d Technology and python" #All Will Be Capital
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3d Technology and python" #All Will Be Small
print(b.capitalize())

# zfill
c,d,e,f = "1", "11" ,"111","1111"
print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

name = "ahmed"
print(name.upper())

# lower()

name2 = "AHMED"
print(name2.lower())