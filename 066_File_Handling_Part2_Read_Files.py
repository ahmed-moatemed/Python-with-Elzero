# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open("D:\كورس\Python with Elzero\\ahmed.txt", "r")

# print(myFile)  # File Data Object
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# print(myFile.read())
# print(myFile.read(11))

# print(myFile.readline(5))
# print(myFile.readline())
# print(myFile.readline())

# print(myFile.readlines())
# print(myFile.readlines(40))
# print(type(myFile.readlines()))


for line in myFile :

  print(line)

  if line.startswith("07") :

    break

# Close The File

myFile.close()