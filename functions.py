def press_grind_beans(): # def defines the function, it is a container for a specified code block
    print("Griding for 20 seconds")
press_grind_beans()

# paramaters give functions thier flexibility using .format(variables)
def cash_withdrawal(amount,accnum):
    print("Withdrawing £{}.00 from {}".format(amount,accnum))
cash_withdrawal(500,12345678)

# defining a fucntion that makes a drink with a specified size
size=["Large","Medium","Small"]
drink=["Coffee","Tea","Water"]
def drink_order(size,drink):
    print("Making a {} sized {}!".format(size,drink))
drink_order(size[0],drink[0])
# or
def drink_order(size,drink):
    print("Making a {} sized {}!".format(size,drink))
drink_order("large","Coffee")

# you can use variables as parameters in functions
# functions can also store data which can be accessed using return
def add(num1,num2):
    return num1+num2
add(7,3)
print(add(7,3))

# you can use different functions together for example for tempearature conversion
def multiply_by_9_fifths(celsius):
    return celsius*(9/5) # return gives back a value from a function, code does not run after calling return
def get_fahrenheit(celsius):
    return multiply_by_9_fifths(celsius)+32
print("The temperature is {} F".format(get_fahrenheit(15)))

def product(num1,num2):
    return num1*num2 
print(product(43,44))

def say_hello(name,age):
    print("Hello, "+name+"! Wow, so you're "+age+" now?")
say_hello("Sasha","30")
# or
def say_hello(name,age):
    print("Hello, {}! Wow, so you're {} now?".format(name,age))
say_hello("Sasha","30")
# or
name=input("What is your name?:")
age=input("How old are you?")
def say_hello(name,age):
    print("Hello, {}! Wow, so you're {} now?".format(name,age))
say_hello(name,age)

def cube(num):
   return num*num*num
print(cube(100)) 
