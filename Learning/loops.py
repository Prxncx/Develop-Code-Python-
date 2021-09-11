fav_site = ["www.mangasail.com","www.youtube.com","www.netflix.com"]
fav_site.append("www.edx.com" and "www.coursera.com")
blocked_site = ["www.fakenews.com","www.boringcode.com","www.madeup.com"]
fav_site.extend(blocked_site)
print(fav_site)
fav_site.count("www.fakenews.com")
print(fav_site.count("www.fakenews.com"))
fav_site.remove(fav_site[-1])
print(fav_site)
fav_site.sort(reverse=True)
print(fav_site)
print(fav_site[-2],fav_site[-3]) #[-n] locates items specifed in the list index going backwards
print(fav_site[0:3]) # [n:n] is where : is used to locate items specified in the list from idex posintion n to n

coordinates=(1,2,3,4) # unlike lists [], tupples () cannot be reassgined or modified
print(coordinates[0]) # you can access elements in a tupple

for i in fav_site: # i specificies the index point of an element in a list
    print(i) # prints each element in specified list individually but not itereable

for i in range(10): # specifies an amount of times to perform a task 
    print("Hello")

for i in range(0,10): # specifies a range of times to perform a task
    print(i)

for i in range(0,10,1): # incriments the range of times to perform a task a specified amount
    print(i)

for i in range(10,-1,-1): 
    print(i)

favourite_films = [
    "Hot Fuzz",
    "Spiderman - Into The Spiderverse",
    "ghostbusters",
    "Shaun of the Dead"
    
]

for i in favourite_films:
    print(i)

def film_check():
    if favourite_films[2] == "Ghostbusters" or favourite_films[2] == "GHOSTBUSTERS" or favourite_films[2] == "ghostbusters":
        print("Yay, Ghostbuster!")
    else:
        print("No Gohostbusters? Boo!")
film_check()

num=0 # specifies num to 0
while num<100: # infinite condition for intstruction, here num is increased to a limit of 100
    num+=5 # contniuously adds 5 to num value (0)
    print(num)

import random
rand_num=random.randint(0,50)
my_num=50

while rand_num != my_num:
    print(rand_num)
    rand_num=random.randint(0,50)
print("Congradulations, you've found {}!".format(my_num))

for i in range(13):
    print("Hello!")
# or
i = 0
while i<13:
    i+= 1
    print("Hello!")

import random
for num in range(6):
    num=random.randint(1,30)
    if num%7==0:
        print(f"{num}'s divisible by 7!")
    else:
        print(f"{num}'s not divisible by 7!")
#
cards=["Diamond","Spade","Club","Heart"]

current_card=random.choice(cards) # random selection in a list
print(current_card)
#
my_card= "Heart"
while current_card != my_card:
    print(current_card)
    current_card=random.choice(cards)
print(f"You've found {my_card}!")
#
random.shuffle(cards)
current_card=cards[random.randint(0,3)]
print(cards)
print(current_card)
#
# cards=list(range(0,25))
# random.shuffle(cards)
# for i in cards:
#     print(i)
# while current_card in range() != i:
#     print("Not Found!")

# A slightly more useful version of the code I posted before
from random import randint
suits = ["Diamond", "Spade", "Club", "Heart"]

def find_suit(wanted_suit):
    current_card = ""

    # Nested helper function
    def random_suit():
        suit = suits[randint(0, 3)]
        print(f"Randomly chosen suit is: {suit}")
        return suit

    while current_card != wanted_suit:
        current_card = random_suit()
        if current_card == wanted_suit:
            print("Found The Correct Suit!")
            return current_card
        else:
            print("That is the wrong suit!")

print() # Print a blank line

print("Looking for a Diamond...")
find_suit("Diamond")

print() # Print a blank line

print("Looking for a Club...")
find_suit("Club")
print()

key="password"
guess = ""
guess_count=0
guess_limit=3
maxed_attempts=False
while guess!=key and not(maxed_attempts):

    if guess_count<guess_limit:
        guess=input("Enter Password: ")
        guess_count+=1
    else:
        maxed_attempts = True

if maxed_attempts:
    print("Maximum allowed attempts reached!")
    print("Password Wrong!")

else:
    print("Password Correct") 