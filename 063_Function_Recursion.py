# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------
# -- To Understand Recursion, You Need To Understand Recursion --
# ---------------------------------------------------------------

# Test Word [ WWWoooorrrldd ] # print(x[1:])

def cleanWord(word) :

  if len(word) == 1 :

    return word
  
  # print(f"Before Condition {word}")
  
  if word[0] == word[1] :

    # print(f"From Condition {word}")

    return cleanWord(word[1:])
  
  # print(f"After Condition {word}")


  return word[0] + cleanWord(word[1:]) # Stach [ World ]


print(cleanWord("WWWoooorrrldd"))