print("Hello, World!")
print("I love Farah Mustapha!")
print("Okay, thanks. Bye!")
# the above line are test strings for the print function
# data types in python include strings "", integers int or float, functions like print
int = 1 # a ssigns integer to 1
float = 1.01234 # assingns float to 1.01234
print(int, float) # prints the specified integer and float
print(len("Hello, World!")) # prints the length of your string
print("I love Farah Mustapha!"[0]) #prints the character at index 0 in your string
#dot notation .() is cused to call on a method
#  .upper() .lower() .capaitalize() .count() .find() .replace() .strip()
# in coding librabries are resources we can use to access code
# import is a function that can be used to access a library
import random # random is a library to a program that generates a random numbers
print(random.random()) # this is how to call on a method with a libraray
print(random.uniform(1,10)) # called on uniform method fromm the random library to generate a number between 1 and 10
print(random.randint(1,10)) # called on randint method in random library
# the follwing lines of code from a practice activity
print("   |   |")
print("   |   |")
print("   |   |")
print("-----------")
print("   |   |")
print("   |   |")
print("   |   |")
print("-----------")
print("   |   |")
print("   |   |")
print("   |   |")
# the following lines of code from a practice activity
print("Sasha".upper()) # prints string in upper case
print("Sasha".lower()) # prints string in lower case
print("Sasha".capitalize()) # prints string with the first character capitalized
print("Sasha".count("a")) # prints the number of times a defined character appears in a string
print("Sasha".find("h")) # prints the first index value for the specified character in the string, -1 is returned if none found
print("Sasha".replace("Sasha", "Daniel")) # prints string replaced with a specifiec value 
print("Sasha".strip("Sasha")) # prints string removing the defined characters adding empty places
print("All around the world"[7].upper())  # [] can used for indexing (specifying an item in code)
my_name = "Sasha Valentine" # = assingns the string to the the value my_name