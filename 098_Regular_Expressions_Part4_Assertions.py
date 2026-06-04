# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ^    Start of String
# #    End Of String
# --------------------------

# Match Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+  for email

# [A-z0-9\.]+@[A-z0-9]+\.(com)   for .com only
# [A-z0-9\.]+@[A-z0-9]+\.(com|net)  for .com, .net

# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$