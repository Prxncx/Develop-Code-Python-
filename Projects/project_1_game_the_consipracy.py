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
   
    sleep(1)
    # Print a blank line after displaying the entire input text
    print("\n")
    
# The code block below pertains to the 1st scene: The Assassination by James. Subject to changes, text art etc. The code block above has not been modified

def start_game():
    print("")
    print("")
    time.sleep(1)
    print("")
    print("")
    type_writer("November 22, 1963. Dallas, Texas.", GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You are John Fitzgerald Kennedy, the 35th president of the United States. You are in Dallas to try to smooth over relations between bickering politicians.",MAGENTA,0.1)
    sleep(1)
    type_writer("You are travelling through downtown Dallas in the back of a convertible. You are surrounded by security, and there is a crowd cheering and waving flags.",MAGENTA,0.1)
    sleep(1)
    type_writer("It is just like many other events just like it. You are surrounded by secret service security agents.",MAGENTA,0.1)
    sleep(1) 
    type_writer("Despite this you feel anxious and unsettled. You recently recieved intelligence that the Soviet Union has obtained compromising material on you",MAGENTA,0.1)
    sleep(1)
    type_writer("There are those, even in your own intelligence agencies, who, you are sure, would see you removed from power- fearing that you may be blackmailed.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Smile and wave to the crowd.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Wave to the crowd and smile",GREEN, 0.1)
    sleep(1) 
    type_writer("3. scan the crowd, and the people around you",GREEN, 0.1)
    sleep(1)
    # convert the player's input() to lower_case
    print("")
    print("")
    answer = input("")

    if "1" in answer:
        jfk1_1()
    elif "2" in answer:
        jfk1_1()
    elif "3" in answer:
        jfk1_2()
    else:
        game_over("INSERT REASON HERE",MAGENTA,0.1)
        sleep(1)

# game_over function accepts an argument called "reason"

def game_over(reason):
    print("")
    print("")
    type_writer("" + reason)
    type_writer("Game Over!",MAGENTA,0.1)
    sleep(1)
    plays_again()

    # function to ask play again or not

def plays_again():
    print("")
    print("")
    type_writer("Do you want to play again? (Y/N)",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    playing_again = input("")
    if "y" or "Y" in playing_again:
        start_game()
    elif "n" or "N" in playing_again:
        exit()
    else:
        plays_again()

def jfk1_1():
    print("")
    print("")
    type_writer("You smile and wave to the crowd. Your wife Jackie does the same. You look out at the sea of waving flags and cheering figures, and the scene takes on a sinister tone.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("You can't put your finger on it, but you feel like something bad is going to happen.",MAGENTA,0.1)
    sleep(1)
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Smile and wave.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Wave and smile.",GREEN, 0.1)
    sleep(1)
                
    # take input()
    print("")
    print("")
    answer = input("")

    if "1" in answer:
        jfk_death()
    elif "2" in answer:
        jfk_death()

def jfk1_2():
    print("")
    print("")
    type_writer("You decide that you shouldn't ignore the discomfiting feeling that you're in danger",MAGENTA,0.1)
    sleep(1)
    type_writer("You look first, at your security detail. They are mostly watching the crowd. Everyone seems relatively relaxed.",MAGENTA,0.1)
    sleep(1)
    time.sleep(2.0)
    print("")
    print("")
    type_writer("Next, you look around. behind you is a large square office building. A book despository or library. A window is open on the sixth floor.",MAGENTA,0.1)
    sleep(1)
    type_writer("You look to your right and you see a crowd of families. A couple of people are filming you.",MAGENTA,0.1)
    sleep(1)
    type_writer("You look to your left, and you see more families watching the procession. You do not notice any threat. You still feel discomfited.",MAGENTA,0.1)
    sleep(1)
    time.sleep(2.0)
    print("")
    print("")
    type_writer("What do you do?",GREEN, 0.1)
    sleep(1)
    type_writer("1. Smile and wave",GREEN, 0.1)
    sleep(1)
    type_writer("2. Wave and smile.",GREEN, 0.1)
    sleep(1)
    # take input()
    print("")
    print("")
    answer = input("")

    if "1" in answer:
        jfk_death()
    elif "2" in answer:
        jfk_death()

def jfk_death():
    print("")
    print("")
    type_writer("Suddenly, you feel like you've been punched hard in your back. You try to exclaim, but you cannot. You look at your wife. She looks horrified.",MAGENTA,0.1)
    sleep(1)
    type_writer("You raise your hands to your throat, and they come away wet with blood. You look desperately to your secret service agents, who are now scrambling towards you to protect you. Your driver also looks to have been shot.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("Before anyone can reach you, your world goes black. You have been shot in the head, and you are dead. The last thing you hear is the scream of your wife.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("TO CONTINUE PRESS Y OR N",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    answer = input("")

    if "y" or "Y" in answer:
        oswald1_1()
    elif "n" or "N" in answer:
        print("")
        print("")
        game_over("Thanks for playing! That was only the intro though. if you continue, there is a whole longer story.",MAGENTA,0.1)
        sleep(1)

def oswald1_1():
    print("")
    print("")
    type_writer("November 22, 1963. Dallas, Texas.",GREEN, 0.1)
    sleep(1)
    type_writer("You are Lee Harvey Oswald, an ex-marine.",MAGENTA,0.1)
    sleep(1)
    type_writer("Until recently, you lived in Belarus after defecting to the Soviet Union. There, you met a wife.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("You found life in the Soviet Union to be dreary. You worked hard but had little to do other than work, and you didn't make many friends",MAGENTA,0.1)
    sleep(1)
    type_writer("You requested to return to the US. In exchange for dropping the charges against you for betraying your country,",MAGENTA,0.1)
    sleep(1)
    type_writer("You were told you would have to do something for the government. At the time, you agreed. How bad could it be?",MAGENTA,0.1)
    sleep(1)
    type_writer("It wasn't until you met your CIA handler, 'Mr Gray' that you realised you may be in over your head",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("He told you that if you wanted to live free in the US with your Belarussian wife, you had to do kill the president.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("That is how you have found yourself on the sixth floor of the Dallas book depository. You got a job here to faciltate your plot.",MAGENTA,0.1)
    sleep(1)
    type_writer("You have a 6.5mm Carcano rifle with a hunting scope. It was provided by your handler.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("The weight of what you're about to do is crushing. You never imagined being in a situation like this. You are nervous and excited.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer(" 1. Steel your nerves.",GREEN, 0.1)
    sleep(1)
    type_writer(" 2. Check your rifle.",GREEN, 0.1)
    sleep(1)

    # take input()
    print("")
    print("")
    answer = input()
    if "1" in answer:
        oswald_nerves()
    elif "2" in answer:
        oswald_rifle()

def oswald_nerves():
    print("")
    print("")
    type_writer("You try to calm down. You try to focus on the task ahead of you. You can't get the idea out of your head that you may be here as a set-up.",MAGENTA,0.1)
    sleep(1)
    type_writer("Even if you shoot the president, how are you going to get away with it?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("You were told that if you don't do it, someone else will, and you will still get the blame.",MAGENTA,0.1)
    sleep(1)
    type_writer("You try to put your misgivings aside. you feel panic rising in your chest.",MAGENTA,0.1)
    sleep(1)
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Take deep breaths, remember your military training.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Focus on the enormity of what you're about to do.",GREEN, 0.1)
    sleep(1)
    
    print("")
    print("")
    answer = input("")
    if "1" in answer:
        oswald_shoot()
    elif "2" in answer:
        oswald_panic()

def oswald_panic():
    

    time.sleep(1)
    type_writer("You think about how world history is going to pivot around your actions in the next few minutes. You hear the motorcade getting closer. You have a panic attack. Your heart is racing, you are shaking, your arms are tingling, and you feel like you are suffocating.",MAGENTA,0.1)
    sleep(1)
    type_writer("You need to calm down, or you won't be able to do anything.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Breathing exercises",GREEN, 0.1)
    sleep(1)
    type_writer("2. Light a cigarette and focus on a comforting memory",GREEN, 0.1)
    sleep(1)

    print("")
    print("")
    answer = input("")
    if "1" in answer:
        oswald_nerves()
    elif "2" in answer:
        oswald_nerves()

def oswald_rifle():
    
    time.sleep(1)
    print("")
    print("")
    print("You check over your rifle. it is relatively new, and in good condition. It is loaded and cocked, with the safety on.",MAGENTA,0.1)
    sleep(1)
    print("However, your handler provided you with a new scope for this mission.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("At the time, you were very nervous and didn't want to spend any more time than you needed to talking to Mr Gray.",MAGENTA,0.1)
    sleep(1)
    type_writer("But now you think about it, he didn't give a very good reason for you to use that scope versus another...",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("You hear the motorcade growing closer.",MAGENTA,0.1)
    sleep(1)
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Get ready to shoot.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Check scope",GREEN, 0.1)
    sleep(1)
    
    print("")
    print("")
    answer = input("")

    if "1" in answer:
        oswald_shoot()
    elif "2" in answer:
        oswald_scope()

def oswald_scope():
    
    type_writer("You check the scope.",MAGENTA,0.1)
    sleep(1)

    time.sleep(1)
    print("")
    print("")
    type_writer("It is a side-mounted 4x18 made by Ordinance Optics. Not exactly top of the line. You wonder why you were provided with this.",MAGENTA,0.1)
    sleep(1)
    type_writer("Upon closer inspection, you realise that the scope itself is slightly misaligned. You cannot fix it here, as the housing itself has been subtly bent.",MAGENTA,0.1)
    sleep(1)
    type_writer("Your mind races. You have been given an inaccurate gun intentionally. Now you really know you are a patsy. You were intended to shoot and miss, while the real assassin makes the kill",MAGENTA,0.1)
    sleep(1)
    type_writer("Your only part in this story is to take the blame for it. You feel betrayed.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer(" What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Abort the mission. If they want to kill the president, they can do it without your help. Maybe you'll be arrested. But they wont have as much evidence.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Make a mental calculation for how to adjust for the inaccurate scope. If you're going to take the blame for killing the president, you may as well kill the president",GREEN, 0.1)
    sleep(1)
    type_writer("3. See if it is possible, to protect the president. watch for threats, and shoot them before they can shoot JFK. Maybe you can get out of trouble if you protect him?",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    answer = input("")
    if "1" in answer:
        oswald_abort()
    elif "2" in answer:
        oswald_adjustshot()
    elif "3" in answer:
        oswald_protect()

def oswald_protect():
   
    
    time.sleep(1)
    print("")
    print("")
    type_writer("You decide you aren't going to play by the CIA's rules. You were never the greatest soldier, or the most loyal citizen, but you'll be damned if you're going to be a tool of the CIA",MAGENTA,0.1)
    sleep(1)
    type_writer("You scan the crowd for threats. You know there must be another assassin, or a CIA observer, and while your chances of spotting them and stopping them are slim, what else can you do?",MAGENTA,0.1)
    sleep(1)
    type_writer("As you look, some movement catches your eye. Behind a grassy gnoll, a policeman is crouched, taking a rifle out of a bag.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("As you watch, the policeman affixes a suppressor to the end of the rifle. You know that this is the second assassin. His bag is the same as the one you were provided.",MAGENTA,0.1)
    sleep(1)
    type_writer("The presidential motorcade is directly below and in front of you, moving along the street. Time is short.",MAGENTA,0.1)
    sleep(1)
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Shoot assassin.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Play your role. Shoot President.",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    answer = input("")
    if answer == "1":
        oswald_shootassassin()
    elif answer =="2":
        oswald_shoot_kill()

def oswald_shootassassin():
    
   
    time.sleep(1)
    print("")
    print("")
    type_writer("You aim at the assassin, as he takes aim at the president. You try to adjust for the scope's being misaligned.",MAGENTA,0.1)
    sleep(1)
    type_writer("You fire!",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("The shot goes wide, impacting the earth about 8 feet to the right of the assassin. He notices the impact, but continues to aim at JFK.",MAGENTA,0.1)
    sleep(1)
    type_writer("You fire twice more, aiming at different points each time. Your last shot lands inches from his head. As you fire the last shot, you see his suppressed rifle jerk in his hands.",MAGENTA,0.1)
    sleep(1)
    type_writer(" swivelling your aim, to look at the motorcade, you see that JFK has been shot badly, and the motorcade is speeding off.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("You try to reaqcuire the assassin in your scope, but he has gone, and so has his rifle.",MAGENTA,0.1)
    sleep(1)
    type_writer("You are acutely aware that it is going to seem like the loud gunshots that coincided with the president being shot will attract a lot of attention to this building very shortly.",MAGENTA,0.1)
    sleep(1)
    type_writer("It is time to leave. What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Drop rifle and leave",GREEN, 0.1)
    sleep(1)
    type_writer("2. Hide rifle and leave",GREEN, 0.1)
    sleep(1)
    answer=input("")
    print("")
    print("")
    if "1" in answer:
        michaelstart()
    elif "2" in answer:
        michaelstart()

def oswald_shoot():
   
 
    time.sleep(1)
    print("")
    print("")
    type_writer("The motorcade comes into view. You tuck yourself into the shadows and raise your rifle",MAGENTA,0.1)
    sleep(1)
    type_writer("You scan the crowd, you see occasional policemen dotted around the crowd. the crowd itself is mostly made up of families.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("As the president's car comes into view you see a little activity off to one side. it looks like a police marksman is getting into position on a grassy knoll to cover the motorcade. He isn't looking at you.",MAGENTA,0.1)
    sleep(1)
    type_writer("To your shock, the president looks around, seemingly looks directly up at your hiding place. You tuck yourself deeper in the shadows and hope he doesn't raise the alarm",MAGENTA,0.1)
    sleep(1)
    type_writer("It is now or never. You affix your crosshairs on the president's back.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Shoot to kill.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Shoot to miss.",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    answer = input("")
    if "1" in answer:
        oswald_shoot_kill()
    elif "2" in answer:
        oswald_shoot_miss()

def oswald_shoot_kill():
    
    
    time.sleep(1)
    print("")
    print("")
    type_writer("You pull the trigger and the rifle jerks in your hands...",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("A cloud of dust to the side of the motorcade puffs up. Secret service agents are alerted by the gunshot and start moving towards the president.",MAGENTA,0.1)
    sleep(1)
    type_writer("You quickly aim and fire again two more times, both times missing. on your third shot, you hear a shot overlap with yours!",MAGENTA,0.1)
    sleep(1)
    type_writer("The president's head jerks to one side and you see a flash of pink mist. He has been shot in the head. You don't think you were the one that did it.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("The crowd starts to panic and scream. The president's car speeds off. You realise quite quickly that you don't have much time to escape.",MAGENTA,0.1)
    sleep(1)
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Hide your rifle and leave",GREEN, 0.1)
    sleep(1)
    type_writer("2. Drop your rifle and leave",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    answer = input("")
    if "1" in answer:
        michaelstart()
    elif "2" in answer:
        michaelstart()

def oswald_shoot_miss():
    
   
    time.sleep(1)
    print("")
    print("")
    type_writer("You aim your sights to the side of the motorcade, intending to miss. You don't want to be responsible for this death.",MAGENTA,0.1)
    sleep(1)
    type_writer("You pull the trigger, and the rifle jerks in your hands.",MAGENTA,0.1)
    sleep(1)
    type_writer("You expected to see a puff of dust, but instead, your bullet seems to hit the driver of JFK's motorcade. Your rifle is inaccurate! you fire two further shots, this time aiming at the president. Both harmlessly skitter off the road. ",MAGENTA,0.1)
    sleep(1)
    type_writer("As you fire your third shot, you hear a shot overlap with yours and the president collapses forward in a cloud of pink mist. You know he is dead. You know you didn't do it.",MAGENTA,0.1)
    sleep(1)
    type_writer("Regardless, you know that the police wouldnt be overly convinced by this argument.",MAGENTA,0.1)
    sleep(1)
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Drop your rifle and hurry out of the room",GREEN, 0.1)
    sleep(1)
    type_writer("2. Carefully hide your rifle and leave the room",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    answer = input("")
    if "1" in answer:
        michaelstart()
    elif "2" in answer:
        michaelstart()

def oswald_adjustshot():
    

    time.sleep(1)
    print("")
    print("")
    type_writer("You finish making your mental adjustments for the scope and fix your sight on the president. You shoot.",MAGENTA,0.1)
    sleep(1)
    type_writer("It misses! you see a cloud of dust kick up somewhere off to the right of the car. The scope was far less accurate than you had thought",MAGENTA,0.1)
    sleep(1)
    type_writer("You fire 2 more times. Each misses. You try to adjust your aim each time, but the gun is simply not consistent. As you are coming to terms with this, you hear another shot overlap with yours.",MAGENTA,0.1)
    sleep(1)
    type_writer("As you watch, the president's head explodes in a pink mist, and he collapses into his wife's lap. You feel sick. It is time to leave",MAGENTA,0.1)
    sleep(1)
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Try to hide the rifle, and leave",GREEN, 0.1)
    sleep(1)
    type_writer("2. Drop the rifle and go.",GREEN, 0.1)
    sleep(1)
    answer = input("")
    if "1" in answer:
        michaelstart()
    elif "2" in answer:
        michaelstart()

def oswald_abort():
    print("")
    print("")
    type_writer("You decide you cannot do it. You are going to abort the mission, and try to forget this ever happened. If the CIA want to punish you, so be it.",MAGENTA,0.1)
    sleep(1)
    type_writer("You uncock your rifle, to make it safe, and you hide it amongst some boxes. As you do this, you hear loud cracks and screams.",MAGENTA,0.1)
    sleep(1)
    type_writer("You look out of the window to see chaos breaking loose. The president's car is speeding off with secret service agents shielding it with their body",MAGENTA,0.1)
    sleep(1)
    type_writer("You see that the president's head is a red ruin. There must have been a second shooter. You need to get out of here.",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    time.sleep(1)
    print("")
    print("")
    type_writer("1. Finish hiding your rifle, and leave",GREEN, 0.1)
    sleep(1)
    type_writer("2. Just leave",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    answer = input("")
    if "1" in answer:
        michaelstart()
    elif "2" in answer:
        michaelstart()
        
# The code block below pertains to the 2nd scene: The Escapre by Michael. Subject to changes, text art etc. The code block above has not been modified

def michaelstart():
 
    print("")
    print("")                         
    type_writer("You now have to leave the depositary on the 6th floor and avoid raising suspicion of your colleagues and detection by the Authoraties best you can.",MAGENTA,0.1)
    sleep(1)
    type_writer("You move towards the lift and stairwell heart racing, sweat profuseley dripping from your brow",MAGENTA,0.1)
    sleep(1)
    type_writer("The blare of sirens draws ever nearer and you realise your window of opportunity to get out unhindered is narrowing with every passing second",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("What do you do?",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("1. Leave in a calm and collected manner",GREEN, 0.1)
    sleep(1)
    type_writer("2. Run for the hills. Exiting the building as quick as humanly possible",GREEN, 0.1)
    sleep(1) 
    type_writer("3. Move to an alternate part of the building and lay low until the coast is clear",GREEN, 0.1)
    sleep(1)
    
    print("")
    print("")
    answer = input("")
    if "1" in answer:
        dep_escape_calm()
    elif "2" in answer:
        dep_escape_run()
    elif "3" in answer: 
        dep_escape_hide()

def dep_escape_calm():
    print("")
    print("")
    type_writer("You make your way down the six flights of stairs, making a momentary stop at the vending machine no the Third floor, grabbing an ice cold can of Coca-Cola from the vending machine to quench your desert dry mouth caused by the adrenaline coursing through your body!",MAGENTA,0.1)
    sleep(1)
    type_writer("By making this pit stop you come face-to-face with a police officer making an initial search of the building!",MAGENTA,0.1)
    sleep(1)
    type_writer("You keep your composure and take a sip of your beverage as the officer demands you identify yourself!",MAGENTA,0.1)
    sleep(1)
    type_writer("Out of nowhere your Boss appears and answers the officer for you. He states you are an employee and for him to continue on up the remaining stairs to the Sixth floor",MAGENTA,0.1)
    sleep(1)
    type_writer("You make quick pleasantries with your Boss and continue calmly on your way down the remaining flights of stairs to the buildings exit.",MAGENTA,0.1)
    sleep(1)
    type_writer("You have made it to the exit, continuing on to Dealey Plaza...",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    the_arrest()

def dep_escape_run():
    print("")
    print("") 
    type_writer("The adrenaline coursing through your veins has got the better of you, initiating one of the most inherent animalistic responses a human can face in a high stress situation…",MAGENTA,0.1)
    sleep(1)
    type_writer("...TO RUN!",MAGENTA,0.1)
    sleep(1)
    type_writer("You dart down all six flights of stairs to the ground floor and burst through the exit doors to outside to make your way to Dealey Plaza.",MAGENTA,0.1)
    sleep(1)
    type_writer("In your state of haste, you fail to recognise your Boss has just witnessed you flee at a rampaging rate.",MAGENTA,0.1)
    sleep(1)
    type_writer("It takes no time at all for him to realise something isn't right and flags down the first Police officer he sees entering the building, informing them of your rapid departure!",MAGENTA,0.1)
    sleep(1)
    type_writer("You are now a person of interest to authorities with a radio transmission sent out for all available units to be on the lookout!",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    the_arrest()

def dep_escape_hide():
    print("")
    print("")
    type_writer("To avoid arousing suspicion by fleeing, no matter how calm or hurried, you move to the employee restroom on the opposite side of the building and hang tight until all officers are in the book depository.",MAGENTA,0.1)
    sleep(1)
    type_writer("You hear all your colleagues making their way to the book depository with officers to get a first hand view of where the assassin may have carried out this heinous crime!",MAGENTA,0.1)
    sleep(1)
    type_writer("Once the coast is clear, you calmly make your way down the remaining flights of stairs and make your way through the exit making your way to Dealey Plaza.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    the_arrest()

# The code block below pertains to the 3rd scene: The Arrest by Sasha. Subject to changes, text art etc. The code block above has not been modified

import sys,time,os

def typewrite(title):
    for char in title:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="":
            time.sleep(0.1)
            sleep(1)
        else:
            time.sleep(0.1)
            sleep(1)

title="THE LEE HARVEY OSWALD RECORD: THE ARREST"

def the_arrest():
    print("")
    print("")
    typewrite(title)
    print("")
    print("")
    dealey_plaza()

def games_over():
    print("")
    print("")
    type_writer("GAME OVER!",GREEN, 0.1)
    sleep(1)
    
    play_again()

def game_cleared():
    print("")
    print("")
    type_writer("GAME CLEARED!",GREEN, 0.1)
    sleep(1)

    next_scence()

def next_scence():
    the_interrogation()

def play_again():
    print("")
    print("")
    type_writer("PRESS Y TO PLAY AGAIN",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    play_again=input("")

    if "y"or"Y" in play_again:
        start_game()
    elif play_again != "y" or "Y":
        games_over()

def dealey_plaza():
    print("")
    print("")
    type_writer("Novemeber 23, 1963",GREEN, 0.1)
    sleep(1)
    type_writer("12:40 PM",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You run acrross Dealey Plaza and two City Buses approach going in opposite directions.",MAGENTA,0.1)
    sleep(1)
    type_writer("Bus 1 is headed to North Oak Cliff and Bus 2 is headed to South Oak Cliff.",MAGENTA,0.1)
    sleep(1) 
    type_writer("Which Bus do you take? ",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("1. Bus 1",GREEN, 0.1)
    sleep(1)
    type_writer("2. Bus 2",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        bus1()
    elif "2" in answer:
        bus2()
    elif input != '1' or '2':
        dealey_plaza()

def bus1():
    print("")
    print("")
    type_writer("Novemeber 23, 1963",GREEN, 0.1)
    sleep(1)
    type_writer("12:50",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You're stuck in heavy traffic, escape is unlikely and paranoia thickens.",MAGENTA,0.1)
    sleep(1) 
    type_writer("Everyone is looking at you, whispering.",MAGENTA,0.1)
    sleep(1) 
    type_writer("You are disgruntled and frustrated so you are going to...",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("1. You ask the driver to let you transfer and take a Taxi Cab",GREEN, 0.1)
    sleep(1)
    type_writer("2. You stay on the bus, it is far too risky to stay in public",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        transfer1_1()
    elif "2" in answer:
        transfer1_2()
    elif input != '1' or '2':
        print
        bus1()

def transfer1_1():
    print("")
    print("")
    home()

def transfer1_2():
    print("")
    print("")
    home()

def bus2():
    print("")
    print("")
    type_writer("Novemeber 23, 1963",GREEN, 0.1)
    sleep(1)
    type_writer("12:50",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You're stuck in heavy traffic, escape is unlikely and paranoia thickens.",MAGENTA,0.1)
    sleep(1) 
    type_writer("Everyone is looking at you, whispering.",MAGENTA,0.1)
    sleep(1) 
    type_writer("You are disgruntled and frustrated so you are going to...",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("1. Ask the driver to let you transfer and take a Taxi Cab",GREEN, 0.1)
    sleep(1)
    type_writer("2. Stay on the bus, it is far too risky to stay in public",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        transfer2_1()
    elif "2" in answer:
        type_writer("Game Over. The reason for Traffic was a blockade setup by Dallas Police.",MAGENTA,0.1)
        sleep(1)
        type_writer("The City Bus you took was raided and the Radio Broadcast instuction was to shoot you on sight.",MAGENTA,0.1)
        sleep(1)
        games_over()
    elif input != '1' or '2':
        bus2()

def transfer2_1():
    print("")
    print("")
    home()

def transfer2_2():
    print("")
    print("")
    games_over()
    print("")
    print("")
    type_writer("Game Over. State Police raided the bus and you were shot and killed on sight!",MAGENTA,0.1)
    sleep(1)

def home():
    print("")
    print("")
    type_writer("Novemeber 23, 1963",GREEN, 0.1)
    sleep(1)
    type_writer("13:00",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You arrive at your stay in. The House keeper Earlene Roberts greets you and makes small talk.",MAGENTA,0.1)
    sleep(1)
    type_writer("There is no time to waste, every second counts and Police sirens are rampant everywhere.",MAGENTA,0.1)
    sleep(1)
    type_writer("You decide to...",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("1. Speak to Earlene, pretend you don't know anything, gather some belongings and catch the next Bus out of town",GREEN, 0.1)
    sleep(1)
    type_writer("2. Ignore Earlene, quickly change clothes, grab your gun, money and catch the next Bus out of town",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        bus_stop1()
    elif "2" in answer:
        bus_stop2()
    elif input != '1' or '2':
        home()

def bus_stop1():
    print("")
    print("")
    type_writer("Novemeber 23, 1963",GREEN, 0.1)
    sleep(1)
    type_writer("13:15",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You're at the bus stop and a Dallas State Police Car drives past you at high speed.",MAGENTA,0.1)
    sleep(1)
    type_writer("The car doubles back and turns around and steers towards you.",MAGENTA,0.1)
    sleep(1)
    type_writer("The Police Car approcahes and pulls up some feet ahead of you",MAGENTA,0.1)
    sleep(1)
    type_writer("As the blinding lights fill you with despair the officer driving speak from the window.",MAGENTA,0.1)
    sleep(1)
    type_writer("He's shouting but you can not hear a thing from the siren.",MAGENTA,0.1)
    sleep(1)
    type_writer("The driver's side door opens as the Police Officer steps out",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("1. The Officer just want's to ask something so you play along ",GREEN, 0.1)
    sleep(1)
    type_writer("2. You are not taking any chances and fire as many rounds as you can into the vehicle",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        print
        type_writer("Dalls Police Officer J. D. Tippit was warning you to dissarm and drop to the ground!",MAGENTA,0.1)
        sleep(1)
        type_writer("You were identified from the description broadcasted on State radio...",MAGENTA,0.1)
        sleep(1)
        game_cleared()
    elif "2" in answer:
        print("")

        type_writer("You left your gun back at your stay-in. Dallas State Police Officer J. D. Tippit shot you dead.",MAGENTA,0.1)
        sleep(1)
        games_over()
    elif input != '1' or '2':
        print("")
        bus_stop1()

def bus_stop2():
    print("")
    print("")
    type_writer("Novemeber 23, 1963",GREEN, 0.1)
    sleep(1)
    type_writer("13:15",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You are at the Bus Stop and a Dallas State Police Car drives past you at high speed.",MAGENTA,0.1)
    sleep(1)
    type_writer("The car doubles back, turns around and steers towards you.",MAGENTA,0.1)
    sleep(1)
    type_writer("The Police Car approcahes and pulls up some feet ahead of you",MAGENTA,0.1)
    sleep(1)
    type_writer("As the blinding lights fill you with despair and the screeching siren fills your ear the officer driving speaks from the window.",MAGENTA,0.1)
    sleep(1)
    type_writer("He's shouting but you can not hear a thing due to the siren.",MAGENTA,0.1)
    sleep(1)
    type_writer("The driver's side door opens as the Police Officer steps out...",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("1. The Officer just want's to ask something so you play along ",GREEN, 0.1)
    sleep(1)
    type_writer("2. You are not taking any chances and fire as many rounds as you can into the vehicle",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        print
        jd_tippit1()
    elif "2" in answer:
        print
        jd_tippit2()
    elif input != '1' or '2':
        print
        bus_stop2()

def jd_tippit1():
    print("")
    print("")
    type_writer("Game Over. Dallas State Officer J. D. Tippit was warning you to dissarm and drop to the ground!",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    games_over()

def jd_tippit2():
    print("")
    print("")
    type_writer("You have killed a State Police Officer, 4 founds went off someone must have heard it all...",MAGENTA,0.1)
    sleep(1)
    type_writer("There are no signs of pursuing Police Units so you...",MAGENTA,0.1)
    sleep(1)
    print("")
    type_writer("1. Look around for witnesses and tie up all loose ends -- the getaway will be clean.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Flee. Run as far away from the area as possible. There's a shoe store nearby you can blend in!",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        print
        shooting1()
    elif "2" in answer:
        print
        shooting2()
    elif input != '1' or '2':
        print
        jd_tippit2

def shooting1():
    print("")
    print("")
    type_writer("Game Over. You were shot dead by Dallas State Police's Emrgency Respose Unit!",MAGENTA,0.1)
    sleep(1)
    type_writer("You acted suspicious, the house keeper Earlene Roberts called the Police immediately after she saw you take your gun and run.",MAGENTA,0.1)
    sleep(1)
    type_writer("She noticed the clothes you wore when you came home fit the suspect's description",MAGENTA,0.1)
    sleep(1)
    type_writer("Earlene watched you gun down Officer J. D. Tippit in cold blood from the window.",MAGENTA,0.1)
    sleep(1)
    type_writer("The Emergency Response Unit watched you across from the across the junction and responded with Leathal Force",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    games_over()

def shooting2():
    print("")
    print("")
    type_writer("Novemeber 23, 1963",GREEN, 0.1)
    sleep(1)
    type_writer("13:30",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You run around the block and stumble into George's Shoe Store.",MAGENTA,0.1)
    sleep(1)
    type_writer("It's quite busy and the manager Jonny Brewer greets you.",MAGENTA,0.1)
    sleep(1)
    type_writer("As sirens get louder, more and more police cars survey the area.",MAGENTA,0.1)
    sleep(1)
    type_writer("Everyone in the store is talking about the shooting at the Motorcade.",MAGENTA,0.1)
    sleep(1)
    type_writer("You are getting sloppy, tired and scared. You have made your mind up...",MAGENTA,0.1)
    sleep(1)
    print("")
    type_writer("1. You have come too far to let it end here, take a hostage and take control. This will work!",GREEN, 0.1)
    sleep(1)
    type_writer("2. Hang back for a bit then leave for the Theatre down the road that should be perfect cover. Nobody should know about the shooting in there.",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        print
        shoe_store1()
    elif "2" in answer:
        shoe_store2()
    elif input != '1' or '2':
        print
        shooting2()

def shoe_store1():
    print("")
    print("")
    type_writer("Game Over. Jonny could smell the danger off you as soon as you walked in, he shoots you the second you reach for your gun.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    games_over

def shoe_store2():
    print("")
    print("")
    type_writer("Novemeber 23, 1963",GREEN, 0.1)
    sleep(1)
    type_writer("13:40",GREEN, 0.1)
    sleep(1)
    print("")
    print("")
    type_writer("You run down to the Texas Theatre and there is nobody at the Ticket Desk so you stroll on in.",MAGENTA,0.1)
    sleep(1)
    type_writer("Dallas State Police Officer Nick McDonald sees this and follows you inside",MAGENTA,0.1)
    sleep(1)
    type_writer("His foot steps echo behind yours so you clasp at your gun",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("1 Do not give the Police Offer a chance to draw his weapon, shoot first! ",GREEN, 0.1)
    sleep(1)
    type_writer("2 You have done a lot of running, you are tired and out of ideas. You put hands up and surrender",GREEN, 0.1)
    sleep(1)
    print("")
    print("")

    answer = input("")

    if "1" in answer:
        print
        theatre1()
    elif "2" in answer:
        print
        theatre2()
    elif input != '1' or '2':
        print
        shoe_store2()

def theatre1():
    print("")
    print("")
    type_writer("Game Over. You fired 4 shots killing Police Officer J. D. Tippit.",MAGENTA,0.1)
    sleep(1)
    type_writer(" Your Gun jammed up and Police Officer Nick Mcdonals shot you dead",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    games_over

def theatre2():
    print("")
    print("")
    type_writer("Game cleared. You are now in custody. You have been baught but you are still alive.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    game_cleared()
    print("")
    print("")

#  The code block below pertains to the Ending part: The Interrogation by Sasha, co scripted by James. Subject to changes, text art etc. The above code block above has not been modified

def ending1():
    expose_conspiracy()

def expose_conspiracy():
    print("")
    print("")
    type_writer("Welldone. The CIA and FBI Agents failed to implicate you in the assasination.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    play_again()

def ending2():
    guilty_conspiracy()

def guilty_conspiracy():
    print("")
    print("")
    type_writer("Unfortunately you implicated yourself in the assassination of President J. F. Kennedy.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    play_again()

# expose ending tally start point:
exposed_conspiracy = []
# guilty ending tally start point:
guilt_conspiracy = []

def the_interrogation():
    room1()

def room1():
    print("")
    print("")
    type_writer("You are dragged through a crowded Police Station, sneered and snarled at.",MAGENTA,0.1)
    sleep(1)
    type_writer("One man to your right side, another clasping to your left side and one more in front.",MAGENTA,0.1)
    sleep(1)
    type_writer("The long, murky corridor can barely accommodate ",MAGENTA,0.1)
    sleep(1)
    type_writer("The walls are stained yellow and the air is filled with the scent of cigarettes.",MAGENTA,0.1)
    sleep(1)
    type_writer("It has a cloying, sticky feel accumulated from years of tar almagamation.",MAGENTA,0.1)
    sleep(1)
    type_writer("The lighting gets darker and darker as you're dragged towards the large unmarked door.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("The door screeches open and you are thrown in.",MAGENTA,0.1)
    sleep(1)
    type_writer("Stumbling back up to your feet, you look around...",MAGENTA,0.1)
    sleep(1)
    type_writer("You notice the shackles on your feet before the two eery shadows standing to the far corners of the room.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("The man in front warns you to not bother trying anything stupid...",MAGENTA,0.1)
    sleep(1)
    question1()

def question1():
    print("")
    print("")
    type_writer("1. Calm down and focus, you are a soldier. You know where this is going, you have been through far worse.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Fight your way to the door, you are not taking the fall for this, you did it for your Country!",GREEN, 0.1)
    sleep(1)
    type_writer("3. Laugh at their faces, you have friends in high places and will make them pay.",MAGENTA,0.1)
    sleep(1)
    
    print("")
    print("")
    question_1 = input("")
    if "1" in question_1:
        exposed_conspiracy.append(1)
    elif "2" in question_1:
        exposed_conspiracy.append(1)
    elif "3" in question_1:
        guilt_conspiracy.append(1)
    else:
        room1()
    room2()

def room2():
    print("")
    print("")
    type_writer("You look around and, pacing yourself. Getting a feel for the room.",MAGENTA,0.1)
    sleep(1)
    type_writer("You see silhouettes behind the frame of glass to your right.",MAGENTA,0.1)
    sleep(1)
    type_writer("The man to you left claps his hands twice. The lights come on, the silhouettes disappear.",MAGENTA,0.1)
    sleep(1)
    type_writer("A large mirror decorates the entire right side of the room floor to ceiling, wall to wall...",MAGENTA,0.1)
    sleep(1)
    question2()

def question2():
    print("")
    print("")
    type_writer("1. Shout to the men in the walls, you won't accept this, you won't be sacrificed.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Demand an Attorney, they can't question you without one",GREEN, 0.1)
    sleep(1)
    type_writer("3. Remain Silent, anything you do or say may and could be used against you",GREEN, 0.1)
    sleep(1)

    print("")
    print("")
    question_2 = input("")
    if "1" in question_2:
        exposed_conspiracy.append(1)
    elif "2" in question_2:
        exposed_conspiracy.append(1)
    elif "3" in question_2:
        guilt_conspiracy.append(1)
    else:
        room2()
    room3()

def room3():
    print("")
    print("")
    type_writer("There are 3 men in the room, all dressed in black.",MAGENTA,0.1)
    sleep(1)
    type_writer("You're with the suits now.",MAGENTA,0.1)
    sleep(1)
    type_writer("The man to your left grabs you by the back of your hair and tells you to sit.",MAGENTA,0.1)
    sleep(1)
    type_writer("The man to your right plays nice and offers you a drink.",MAGENTA,0.1)
    sleep(1)
    question3()

def question3():
    print("")
    print("")
    type_writer("1. Take a seat and accept the drink.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Take a seat and refuse the drink.",GREEN, 0.1)
    sleep(1)
    type_writer("3. Take a seat and stay silent.",GREEN, 0.1)
    sleep(1)

    print("")
    print("")
    question_3 = input("")
    if "1" in question_3:
        exposed_conspiracy.append(1)
    elif "2" in question_3:
        exposed_conspiracy.append(1)
    elif "3" in question_3:
        guilt_conspiracy.append(1)
    else:
        room3()
    room4()

def room4():
    print("")
    print("")
    type_writer("There is only one chair in the room facing the large mirror. You drag your feet in slouch into it.",MAGENTA,0.1)
    sleep(1)
    type_writer("The man in front stands behind you and lights a cigarette as he postures against the wall.",MAGENTA,0.1)
    sleep(1)
    type_writer("He offers you a cigarette and gestures his pack to you...",MAGENTA,0.1)
    sleep(1)
    question4()

def question4():
    print("")
    print("")
    type_writer("1. Sure, why not it might be my last one.",GREEN, 0.1)
    sleep(1)
    type_writer("2. Hell no, this is not my first rodeo. I have no idea where that thing has been.",GREEN, 0.1)
    sleep(1)
    type_writer("3. Look away and stay silent.",GREEN, 0.1)
    sleep(1)

    print("")
    print("")
    question_4 = input("")
    if "1" in question_4:
        exposed_conspiracy.append(1)
    elif "2" in question_4:
        exposed_conspiracy.append(1)
    elif "3" in question_4:
        guilt_conspiracy.append(1)
    else:
        room4()
    room5()

def room5():
    print("")
    print("")
    type_writer("Man on the left: Let us cut to the chase.",MAGENTA,0.1)
    sleep(1)
    type_writer("Man on the left: Tell us why you killed the President.",MAGENTA,0.1)
    sleep(1)
    question5()

def question5():
    print("")
    print("")
    type_writer("1. Deny",GREEN, 0.1)
    sleep(1)
    type_writer("2. Reveal ",GREEN, 0.1)
    sleep(1)
    type_writer("3. Stay silent",GREEN, 0.1)
    sleep(1)

    print("")
    print("")
    question_5 = input("")
    if "1" in question_5:
        exposed_conspiracy.append(1)
    elif "2" in question_5:
        exposed_conspiracy.append(1)
    elif "3" in question_5:
        guilt_conspiracy.append(1)
    else:
        room5()
    room6()

def room6():
    print("")
    print("")
    type_writer("Man on the right: Give it up already, we know what you did, how you did it and when you did it.",MAGENTA,0.1)
    sleep(1) 
    type_writer("Man of the right: All we want to know is who else was involved. The Chinese? The Russians? The Mafia?",MAGENTA,0.1)
    sleep(1)
    question6()

def question6():
    print("")
    print("")
    type_writer("1. Deny",GREEN, 0.1)
    sleep(1)
    type_writer("2. Reveal ",GREEN, 0.1)
    sleep(1)
    type_writer("3. Stay silent",GREEN, 0.1)
    sleep(1)

    print("")
    print("")
    question_6 = input("")
    if "1" in question_6:
        guilt_conspiracy.append(1)
    elif "2" in question_6:
        guilt_conspiracy.append(1)
    elif "3" in question_6:
        guilt_conspiracy.append(1)
    else:
        room6()
    room7()

def room7():
    print("")
    print("")
    type_writer("Man behind you: Who are you working for, Commie? No way grunt like you could pull this off without some serious weight behind you!",MAGENTA,0.1)
    sleep(1) 
    type_writer("Man behind you: It's those Russians isn't it. There is a war coming and you know it!",MAGENTA,0.1)
    sleep(1)
    question7()

def question7():
    print("")
    print("")
    type_writer("1. Deny",GREEN, 0.1)
    sleep(1)
    type_writer("2. Reveal ",GREEN, 0.1)
    sleep(1)
    type_writer("3. Stay silent",GREEN, 0.1)
    sleep(1)
    
    print("")
    print("")
    question_7 = input("")
    if "1" in question_7:
        guilt_conspiracy.append(1)
    elif "2" in question_7:
        exposed_conspiracy.append(1)
    elif "3" in question_7:
        exposed_conspiracy.append(1)
    else:
        room7()
    room8()

def room8():
    print("")
    print("")
    type_writer("Man of the left: We know about the calls and visits to the Embassy",MAGENTA,0.1)
    sleep(1)
    type_writer("Man on the left: I'll ask again, did the Russians put you up to this?",MAGENTA,0.1)
    sleep(1)
    question8()

def question8():
    print("")
    print("")
    type_writer("1. Deny",GREEN, 0.1)
    sleep(1)
    type_writer("2. Reveal ",GREEN, 0.1)
    sleep(1)
    type_writer("3. Stay silent",GREEN, 0.1)
    sleep(1)
    
    print("")
    print("")
    question_8 = input("")
    if "1" in question_8:
        exposed_conspiracy.append(1)
    elif "2" in question_8:
        guilt_conspiracy.append(1)
    elif "3" in question_8:
        guilt_conspiracy.append(1)
    else:
        room8()
    room9()

def room9():
    print("")
    print("")
    type_writer("Man on the right: Hang on Hosty, maybe we can sweeten him up a little",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Man on the left: Captain Fritz, Sir if we lay a hand on him the Press will not let this go",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Man behind you: Haha. That's not what he meant, Hoover. But beating the life out of a Commie sounds about as American as this gets",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Hoover: Then what are we doing with him?",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Captain Fritz: He's a Soviet Spy, enemy of the United States. We can do whatever we want",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Hosty: You picked the wrong side, buddy. Once we get what we want you're done for so better talk now.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("captain fritz: Dead men tell no ties",MAGENTA,0.1)
    sleep(1)
    question9()

def question9():
    print("")
    print("")
    type_writer("1. Deny",GREEN, 0.1)
    sleep(1)
    type_writer("2. Reveal ",GREEN, 0.1)
    sleep(1)
    type_writer("3. Stay silent",GREEN, 0.1)
    sleep(1)
    
    print("")
    print("")
    question_9 = input("")
    if "1" in question_9:
       exposed_conspiracy.append(1)
    elif "2" in question_9:
        guilt_conspiracy.append(1)
    elif "3" in question_9:
        guilt_conspiracy.append(1)
    else:
        room9()
    room10()

def room10():
    print("")
    print("")
    type_writer("Captain Fritz: We have the rifle. Your fingerprints and witnesses that placed you at the Book Depository.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Hosty: We already tracked your movement to anf from Dealey Plaza.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Hoover: A witness saw you on the 6th Floor of the Texas School Book Depisitory at 11:30",MAGENTA,0.1)
    sleep(1)
    type_writer("Hoover: Another saw you on the first floor at 11:50 and one more at 12:00.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Hosty: At 12:10 you were again seen on the 1st Floor.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Captain Fritz: At 12:30 A fourth witness saw you aiming a rifle out of the 6th Floor.",MAGENTA,0.1)
    sleep(1)
    type_writer("Captain Fritz: A City Bus Driver indentified you boarding his Bus at 12:40 in Dealey Plaza",MAGENTA,0.1)
    sleep(1)
    type_writer("Captain Fritz: A Taxi Driver verified that you took his service at 13:00 ti 1026 North Beckley",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Hoover: At 13:15 Dallas Police Officer J. D. Tippit identified you at your residence and was murdered.",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Hosty: The bullet signature matched those on the firearm you were carrying at point of arrest at 13:40!",MAGENTA,0.1)
    sleep(1)
    type_writer("Hosty: Before that you were identified by a shoe store manager at 13:35",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Captain Fritz: Right down the rabbit hole..",MAGENTA,0.1)
    sleep(1)
    type_writer("Captain Fritz: We have got you sucker!",MAGENTA,0.1)
    sleep(1)
    print("")
    print("")
    type_writer("Hosty: Now stop wasting our time and tell us everything we want to know...",MAGENTA,0.1)
    sleep(1)
    question10()

def question10():
    print("")
    print("")
    type_writer("1. Deny",GREEN, 0.1)
    sleep(1)
    type_writer("2. Reveal ",GREEN, 0.1)
    sleep(1)
    type_writer("3. Stay silent",GREEN, 0.1)
    sleep(1)
    
    print("")
    print("")
    question_10 = input("")
    if "1" in question_10:
       guilt_conspiracy.append(1)
    elif "2" in question_10:
        exposed_conspiracy.append(1)
    elif "3" in question_10:
        guilt_conspiracy.append(1)
    else:
        room10()

def score_game():
    if len(guilt_conspiracy) > len(exposed_conspiracy):
        ending2()
    elif len(guilt_conspiracy) == len(exposed_conspiracy):
        ending2()
    elif len(exposed_conspiracy) > len(guilt_conspiracy):
        ending1()

start_game()
score_game()
type_writer("You gave:",MAGENTA,0.1)
sleep(1)
print("")
print("")
print(len(exposed_conspiracy))
print("")
print("")
type_writer("Absolving Responses compared to:",MAGENTA,0.1)
sleep(1)
print(len(guilt_conspiracy))
print("")
print("")
type_writer("Implicating Responses.",MAGENTA,0.1)
sleep(1)