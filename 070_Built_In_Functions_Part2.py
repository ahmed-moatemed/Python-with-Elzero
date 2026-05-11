# -----------------------
# -- Built In Function --
# -----------------------
# sum() 
# round() 
# range() 
# print() 
# -----------------------

# sum(iterable, start)

a = [1, 10, 19, 40]
print(sum(a))
print(sum(a, 20))

# round(number, numofdigits)
print(round(100.389))
print(round(100.389, 2))
print(round(100.389, 4))

# range(start, end, step)
print(list(range(0)))
print(list(range(11)))
print(list(range(1,11,2)))

# print()
# print("Hello @ Ahmed @ How @ Are @ You")
# print("Hello","Ahmed","How","Are","You", sep=" | ")

print("First Line", end=" ")
print("Seconde Line", end="\\")
print("Third Line")