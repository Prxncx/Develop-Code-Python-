from time import sleep
import sys
import os
import random

combination_tried = False
player_score = 0
player_name = "User"

# Clears the terminal when called
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# These constants are required for the type writer function
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

# Prints a string to the terminal one letter at a time. The default value for text is an empty string to prevent any errors
def type_writer(text = "", colour = WHITE, speed = 0.03):
    for i in text:
        # Don't worry about this code. It's looks a little bit complicated but it seems to work...
        output = "\x1b[1;%dm" % (30+colour) + i + "\x1b[0m"
        sys.stdout.write(output)
        sys.stdout.flush()
        
        # Wait for a fraction of a second before displaying the next letter
        sleep(speed)
   
    sleep(0.5)
    # Print a blank line after displaying the entire input text
    print("\n")


p1 = "November 22, 1963. Dallas, Texas.\n\nYou are John Fitzgerald Kennedy, the 35th president of the United States. You are in Dallas to try to smooth over relations between bickering politicians.\n\nYou are travelling through downtown Dallas in the back of a convertible. You are surrounded by security, and there is a crowd cheering and waving flags.\n\nIt is just like many other events just like it. You are surrounded by secret service security agents.\n\nDespite this you feel anxious and unsettled. You recently recieved intelligence that the Soviet Union has obtained compromising material on you\n\nThere are those, even in your own intelligence agencies, who, you are sure, would see you removed from power- fearing that you may be blackmailed.\n\n"

q1 = "What do you do?"

a1 = [
    "1. Smile and Wave", 
    "2. Wave and Smile" ]

p2 = "You smile and wave to the crowd. Your wife Jackie does the same. You look out at the sea of waving flags and cheering figures, and the scene takes on a sinister tone.\n\nYou can't put your finger on it, but you feel like something bad is going to happen.\n\n"

q2 = "What do you do?"

a2 = [
    "1. Smile and Wave", 
    "2. Wave and Smile" 
    ]

p3 = "You decide that you shouldn't ignore the discomfiting feeling that you're in danger.\n\nYou look first, at your security detail. They are mostly watching the crowd. Everyone seems relatively relaxed.\n\nNext, you look around. behind you is a large square office building. A book despository or library. A window is open on the sixth floor.\n\nYou look to your right and you see a crowd of families. A couple of people are filming you.\n\nou look to your left, and you see more families watching the procession. You do not notice any threat. You still feel discomfited.\n\n"

q3 = "What do you do?"

a3 = [
    "1. Smile and Wave", 
    "2. Wave and Smile" 
    ]

p4 = "Suddenly, you feel like you've been punched hard in your back. You try to exclaim, but you cannot. You look at your wife. She looks horrified.\n\nYou raise your hands to your throat, and they come away wet with blood. You look desperately to your secret service agents, who are now scrambling towards you to protect you. Your driver also looks to have been shot.\n\nBefore anyone can reach you, your world goes black. You have been shot in the head, and you are dead. The last thing you hear is the scream of your wife."

def continue_play():
    print("\n\n")
        answer = input("")

        if "y" or "Y" in answer:
            oswald1_1()
        elif "n" or "N" in answer:
            print("")
            print("")
            game_over("Thanks for playing! That was only the intro though. if you continue, there is a whole longer story.",MAGENTA,0.03)
            sleep(0.5)

continue_play()

p5 = "November 22, 1963. Dallas, Texas.\n\nYou are Lee Harvey Oswald, an ex-marine.\n\nUntil recently, you lived in Belarus after defecting to the Soviet Union. There, you met a wife.\n\nYou found life in the Soviet Union to be dreary. You worked hard but had little to do other than work, and you didn't make many friends.\n\nYou requested to return to the US. In exchange for dropping the charges against you for betraying your country.\n\nYou were told you would have to do something for the government. At the time, you agreed. How bad could it be?\n\nIt wasn't until you met your CIA handler, 'Mr Gray' that you realised you may be in over your head.\n\nHe told you that if you wanted to live free in the US with your Belarussian wife, you had to do kill the president.\n\nThat is how you have found yourself on the sixth floor of the Dallas book depository. You got a job here to faciltate your plot.\n\nYou have a 6.5mm Carcano rifle with a hunting scope. It was provided by your handler.\n\nThe weight of what you're about to do is crushing. You never imagined being in a situation like this. You are nervous and excited."

q5 = "What do you do?"

a5 = [
    "1. Steel your nerves", 
    "2. Check you rifle"
    ]

p6 = "You try to calm down. You try to focus on the task ahead of you. You can't get the idea out of your head that you may be here as a set-up.\n\nEven if you shoot the president, how are you going to get away with it?\n\nYou were told that if you don't do it, someone else will, and you will still get the blame.\n\nYou try to put your misgivings aside. you feel panic rising in your chest."

q6 = "What do you do?"

a6 = [
    "1. Take deep breaths, remember your military training.",
    "2. Focus on the enormity of what you're about to do."
    ]

p7 = "You think about how world history is going to pivot around your actions in the next few minutes. You hear the motorcade getting closer.\n\nYou have a panic attack. Your heart is racing, you are shaking, your arms are tingling, and you feel like you are suffocating.\n\nYou need to calm down, or you won't be able to do anything."

q7 = "What do you do?"

a7 = [
    "1. Breathing exercises",
    "2. Light a cigarette and focus on a comforting memory"
]

p8 = 