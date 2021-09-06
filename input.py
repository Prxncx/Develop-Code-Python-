mynum=447534400666
print(str(mynum)) # returns the variable as a string
# max(8,7) returns the largest of the values 
# min(8,7) or floor() returns the lowest of the values
# round(4.3) round to the neareast integer
# sqrt() returns the square root of a number
from math import * # imports * functions from math library
name=input("Enter your name:") # stores input in variable defined name
print("Hello, {}!".format(name)) # prints the declared variable in the {} defined format

num1=input("Enter a number:") # stores input
num2=input("Enter another number:") # stores input again
result=num1+num2 # adding the 2 inputs together
print(result) # python stores input as strings 
result = int(num1)+int(num2) # int() converts stored strings to integers
result = float(num1)+float(num2) # converts stored string to float
print(result)

colour=input("Enter a colour:")
plural_noun=input("Enter a plural noun:")
celebrity=input("Enter a celebrity:")

print("Roses are "+colour)
print(plural_noun+" are blue")
print("I love "+celebrity)