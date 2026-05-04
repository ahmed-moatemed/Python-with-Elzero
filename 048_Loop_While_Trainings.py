# ----------------------------
# -- Loop => While Training --
# ----------------------------
# While Condition_is_true
#   Code Will Run Until Condition Become False
# ----------------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF)) # List Length

a = 0

while a < len(myF) :

  print(f"#{str(a + 1).zfill(2)} {myF[0]}")

  a += 1

else :

  print("All Friends Printed.")

