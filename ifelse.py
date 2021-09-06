speed="fast"
speed="cruise"
speed="slow"

if speed=="fast":
    print("Please, slow down!")
elif speed=="slow":
    print("Come on, go faster!")
else: 
    print("I love these kinds of drives!")

# ==, !=
# >, !>
# <, <!
# ||, or
# ++, and
# >=, !>=
# <=, !<=
# ! negative opereator

age=21
if age>=17:
     print("Yes, ofcourse I will serve you!")
else:
    print("I'm sorry, you are not old enough!")

country = ["United Kingdon", "United States", "Thailand"]

country = country[0]
if country==country[1] and age<=17:
     print("Sorry, I can't serve you at that age here!")
elif country==country[1] and age>=17:
    print("Sorry, wait anothet year!")
else:
    print("It's on the house!")

day=["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend =day[0] or day[1]

day = day[2]

if day==day[0] or day==day[1]:
     print("It's the Weekend!")
else:
    print("It's a weekday!")

if day!=day[0] or day!=day[1]:
     print("Ugh, I can't wait for the weekend")
else:
    print("Ugh, I wish weekend was longer!")

password = "chocolate" 
if len(password)<=8:
    print("Passowrd too short!")
else:
    print(password)

num = 178
if num%3==0 or num%5==0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")

num = 687
if num%3==0: 
    print("Fizz")
elif num%7==0:
    print("Buzz")
elif num%3==0 and num%7==0:
    print("Fizz Buzz")
else:
    print(num)

word = "Python"
if word[-1]==word[0]:
    print(True)
else:
    print(False)

time=7
place_of_work = "Apple"
town_of_home = "Cupertino"
if time>=8 and time<=17:
    print(f"I'm at {town_of_home}")
elif time <=8:
    print("I'm in bed stop calling me!")
else:
    print(f"I'm at work {place_of_work}")

num1=88
num2=23
num3=num1+num2
if num3%2==0:
    print("Congrats! The answer is even")
else:
    print("Try again")
# or
num1=88
num2=23
num3=num1+num2 # n%2==0 checks if the number is even, n%n==0 checks if the number is odd, n%i==0 checks if the number is a prime
if (num1+num2)%2==0: # use paranthesis for proper structure
    print("Congrats! The answer is even")
else:
    print("Try again")

# extra challenges