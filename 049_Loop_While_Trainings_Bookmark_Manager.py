# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill Later 
myFavouriteWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0 :

  # Input The New Website
  web = input("Website Name Without https:// ").strip()

  # Add The New Website To The List
  myFavouriteWebs.append(f"https://{web.lower()}")

  # Decrease One Number From Allowed Websites
  maximumWebs -= 1

  # Print The Add Message
  print(f"Wedsite Add, {maximumWebs} Places Left")

  # Print The List 
  print(myFavouriteWebs)

else :

  print("Done..")

# Check If List Is Not Empty
if len(myFavouriteWebs) > 0 :

  # Sort The List
  myFavouriteWebs.sort()

  index = 0

  print("Printing The List Of Websites")

  while index < len(myFavouriteWebs) :

    print(myFavouriteWebs[index])

    index += 1