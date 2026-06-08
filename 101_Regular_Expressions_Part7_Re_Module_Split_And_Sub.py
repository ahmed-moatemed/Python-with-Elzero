# ----------------------------------------------------
# -- Regular Expressions => Re Module Split and Sub --
# ----------------------------------------------------
# split(pattern, string, maxsplit) => Return A List of Elements Splitted on Each Match
# sub(pattern, replace, string, ReplaceCount) => replace matches With What You Want
# ----------------------------------------------------

import re

string_One = "I Love Python and My Self"

search_One = re.split(r"\s", string_One, 3)

print(search_One)

print("#" * 40)

string_Two = "How-To_Write_A_Very-Good-Article"

serach_Two = re.split(r"-|_", string_Two)

print(serach_Two)

print("#" * 40)

# Get Words From URL

for counter, word in enumerate(serach_Two,1):

    if len(word) == 1:

        continue

    print(f"Word Number: {counter} => {word.lower()}")

print("#" * 40)

my_String = "I Love You"

print(re.sub(r"\s", "-", my_String, 1))