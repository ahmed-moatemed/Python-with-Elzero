# -------------------------------------------------
# -- Practical => Loop On Many Iterators With Zip() --
# -------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length Of Lowest Object
# -------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Ahmed", "Age": 23, "Country": "Egypt", "Skill": "Python"}


for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1) :

  print(f"'1' {item1} => '2' {item2} => '3' {item3} => '4' Key => {item4}, value => {dict1[item4]}")




# ultimateList = zip(list1, list2)
# print(ultimateList)
# for i in ultimateList :
#   print(i)