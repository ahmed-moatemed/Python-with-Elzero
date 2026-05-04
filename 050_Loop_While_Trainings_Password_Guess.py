# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4

mainPassword = "Ahmed@123"

inputPassword = input("Write Your Password: ")

while inputPassword != mainPassword :

  tries -= 1

  print(f"Wrong Password, {'Last' if tries == 0 else tries} Chance")

  inputPassword = input("Write Your Password: ")

  if tries == 0:

    print("All Tries Is Finished.")

    break

else :

  print("Correct Password")

