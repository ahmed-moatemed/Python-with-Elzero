# -------------
# -- Numbers --
# -------------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(0))

# Float

print(type(1.5888))
print(type(100.99))
print(type(0.99))
print(type(-10.99))
print(type(-0.99))

# Complex

myComplexNumber = 5+6j

print(type(myComplexNumber))

print("Real Part is: {}".format(myComplexNumber.real))
print("Imaginary Part is: {}".format(myComplexNumber.imag))


# [1] you Can Convert From Int To Float Or Complex
# [2] You Can Convert From Float To Int Or Complex
# [3] You Can't Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
# print(int(10+9j)) # Error
# print(float(10+9j)) # Error