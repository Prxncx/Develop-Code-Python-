my_name = "Sasha Valentine" # = assigns the string to the the value my_name
my_age = 18 # assigns the integer to the the value my_age
student = True # defines value to true
student = False # defines value to false
print(my_name)
print(my_age)
print(student)
# connecting words with _ is called snake_case this is an appopriate wat to name variables in code
fav_manga = "Berserk"
print("My favourite manga is", fav_manga) 
print("My favourite manga is " + fav_manga) # + only works twoth the dame data type
# .format() is a method you can use {} to create sensible outputs 
print("My favourite manga is {}".format(fav_manga))
print("My name is {} and my favourite manga is {} ".format(my_name, fav_manga))
print("\"Hello\" said Liam") # \ = escape character, breaks the strong format for textual quotation
# * / - ** % || = > < are some arithmatic operators 
x = 10 # assigns x to a value of 10
x = x+x # assigns x to a value of x + 10
x += 2 # adds 2 to the value of x + x
print(x) # returns the current value of x
print("my name is {} and my favourite manga is {} ".upper().format(my_name.upper(), fav_manga.upper()))
# OR
print("my name is {} and my favourite manga is {} ".upper().format(my_name, fav_manga).upper())
user_name = "Farah Mustapha"
fav_colour = "Black"
user_age = 33

breakfast = ["cereal", "full english", "nothing"]
lunch = ["tea", "coffee", "nothing"]
dinner = ["rice", "pasta", "salad"]

print("My name is {}, I am {} years old and my favourite colour is {}".format(user_name, user_age, fav_colour))
print("Today I ate {} for breakfast, {} for lunch and {} for dinner".format(breakfast[0], lunch[1], dinner[1]))
print("Tomorrow I may have {} for breakfast, {} for lunch and {} for dinner".format(breakfast[2], lunch[1], dinner[2]))

space1 = "X"
space2 = "O"
space3 = "X"
space4 = "O"
space5 = "O"
space6 = "O"
space7 = "X"
space8 = "O"
space9 = "X"
print(f"  {space1}  |  {space2}  |  {space3}  ") # print(f" ") 
print(f"----------------")
print(f"  {space4}  |  {space5}  |  {space6}  ")
print(f"----------------")
print(f"  {space7}  |  {space8}  |  {space9}  ")

import datetime
today_date = datetime.date(2021, 6, 12)
birth_date = datetime.date(1991, 6, 12)
days_old = today_date - birth_date
print(f"I am {days_old.days} days old")
# or
from datetime import date
print(f"I am {days_old.days} days old")