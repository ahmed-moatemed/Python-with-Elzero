# ----------------------------------
# -- Ternary Condirional Operator --
# ----------------------------------

country = "Egypt"

if country == "Egypt": print(f"The Weather in {country} is 15")
elif country == "KSA": print(f"The Weather in {country} is 30")
else :print("Country is Not in The List")

# Short If

movieRate = 18
age = 15 

if age < movieRate :

  print("Movie S Not Good 4U") # Condition If True

else:
  
  print("Movie S Good 4U And Happy Watching") # Condition If False

print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Conditon | Else | Condition If False