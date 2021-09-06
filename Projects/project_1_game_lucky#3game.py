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

# Start game function. This gets called at the end of the file.
def game_start():
    # Clear the terminal ready for the new scene
    clear()

    sleep(1)
    print("""\033[32m
    
                                                                                                                                  @@@@@@@                                                                 
                                                                                                                               @@@@@@@@@@@@@                                                            
                                                                                                                             @@@@@@@@@@@@@@@@@                                                          
                                                                                                                            @@@@@@@@@@@@@@@@@@@                                                         
                                                                                                                            @@@@@@@@@@@@@@@@@@@                                                         
                                                                                                                            /@@@@@@@@@@@@@@@@@                                                          
                                                                                                                              @@@@@@@@@@@@@@@                                                           
                                                                                                                                ,@@@@@@@@@,                                                             
                                                                                                                                    @@@                                                                 
                                                                                                                                    @@@                                                                 
                                                                                                                                    @@@                                                                 
                                                                                                                                    @@@                                                                 
                                                                                                                                    @@@                                                                 
                                                                                                                                    @@@                                                                 
                                                                                                                                    @@@                                                                 
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@                                                                 
@@                                                                                                                          @@      @@@                                                                 
@@                                                                                                                          @@      @@@                                                                 
@@     @                                   @                                     @                                     @    @@      @@@                                                                 
@@     @                                   @                                     @                                     @    @@      @@@                                                                 
@@     @          /@@@@@@@@@@@@/           @                                     @                                     @    @@      @@@                                                                 
@@     @               @@@@.               @                   @       @         @               @@@@@@@@@@@           @    @@      @@@                                                                 
@@     @              )@@@(                @                  @       @          @             @%        @@@@@         @    @@@@@@@@@@@@@                                                               
@@     @              @@@@                 @                 @@      @@          @                        @@@@         @    @@@@@@@@@@@@@@                                                              
@@     @             /@@@@                 @            @@@@@@@@@@@@@@@@@@@      @                        @@@@         @    @@@@@@@@@@@@@@@                                                             
@@     @             @@@@                  @          %@@@@@@@@@@@@@@@@@@@       @                       @@@           @    @@@@@@@@@@@@@@@                                                             
@@     @             @@@@                  @               @       @             @                     @@              @    @@@@@@@@@@@@@@@                                                             
@@     @            @@@@                   @              @       @              @               .@@@@@@@@             @    @@@@@@@@@@@@@@@                                                             
@@     @            @@@@                   @             @@      @@              @                     @@@@@@          @    @@@@@@@@@@@@@@@                                                             
@@     @           @@@@                    @       @@@@@@@@@@@@@@@@@@@@          @                       @@@@@         @    @@@@@@@@@@@@@@@                                                             
@@     @           @@@@                    @      %@@@@@@@@@@@@@@@@@@@           @                        @@@@         @    @@@@@@@@@@@@@@@                                                             
@@     @          @@@@                     @           @       @                 @                        @@@@         @    @@@@@@@@@@@@@@@                                                             
@@     @          @@@@                 @   @          @@      @@                 @                       @@@@          @    @@@@@@@@@@@@@@@                                                             
@@     @         @@@@(               @@    @         @@      @@                  @       @,             @@@            @    @@@@@@@@@@@@@@                                                              
@@     @        @@@@@@             @@@     @                                     @      @@@@@&       &@@               @    @@@@@@@@@@@@                                                                
@@     @    @@@@@@@@@@@@@@@@@@@@@@@@@      @                                     @         (@@@@@@(                    @    @@                                                                          
@@     @                                   @                                     @                                     @    @@                                                                          
@@     @                                   @                                     @                                     @    @@                                                                          
@@                                                                                                                          @@                                                                          
@@                                                                                                                          @@                                                                          
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                          
                                                                                                                                                                                                                                                                                                                                                      
    """)
    sleep(1)
    type_writer("LUCKY NUMBER 3", GREEN, 0.1)
    sleep(1)
    type_writer("Press Enter to Continue...", BLUE)
    input()
    scene_1()


# Scene One
def scene_1():
    # Clear the terminal ready for the new scene
    clear()

    type_writer("Last night you went to a poker game.")
    # Wait for a second in between lines
    sleep(1)
    
    type_writer("The cards were not stacked in your favour.")
    # Wait for a second in between lines
    sleep(1)
    
    type_writer("After you got home you decided to drown your sorrows.")
    # Wait for a second in between lines
    sleep(1)

    type_writer("Unfortunately, you also obliterated your short term memory.")
    # Wait for a second in between lines
    sleep(1)

    type_writer("You’re sitting at a blackjack table warming up for another night on the strip.")
    # Wait for a second in between lines
    sleep(1)

    type_writer("You hope your luck is better tonight.")
    # Wait for a second in between lines
    sleep(1)

    type_writer("An old Texan playing on the same table table seems to be impressed with your skills.")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"That's some fancy counting there son!\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"What did you say your name was?\"", YELLOW)

    name_input()


# This part of scene one has been split into a separate function. This is so that we can ask for the player name again if the player tries to enter a blank name
def name_input():
    # Let the player input a name
    global player_name
    player_name = input()
    print()
    if player_name:
        type_writer(f"\"{player_name}? That's a stupid sounding name!\"", CYAN)
        # Wait for a second in between lines
        sleep(1)
        type_writer("Press Enter To Continue...", BLUE)
        input()
        scene_2()
    else:
        type_writer("\"I'm sorry son... I didn't hear that.\"")
        # Wait for a second in between lines
        sleep(1)
        type_writer("\"I'm a bit deaf from all the shooting I do.\"")
        # Wait for a second in between lines
        sleep(1)
        type_writer("\"What did you say your name was?\"", YELLOW)
        # Wait for a second in between lines
        sleep(1)
        # Call this same function again to give the player another attempt at entering a name
        name_input()


# Scene 2
def scene_2():
    global player_name
    
    # Clear the terminal ready for the new scene
    clear()

    type_writer("You play another couple of rounds. As you're playing you become aware of a buzzing sound in your ear.")
    # Wait for half a second in between lines
    sleep(0.5)

    type_writer("The buzzing almost sounds like someone speaking...")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"What was the plan again?\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("The voice is that of your old friend The Acrobat.")
    # Wait for a second in between lines
    sleep(1)
    
    type_writer("The two of you have a history of \'Felonious Activity\'...")
    # Wait for a second in between lines
    sleep(1)

    type_writer("Your start to feel a sinking feeling inside as you realise this might be one of those occasions... You can't remember the plan!")
    # Wait for a second in between lines
    sleep(1)

    type_writer("You ask the dealer \"What are my options\" hoping The Acrobat will hear this and jog your memory.")
    # Wait for a second in between lines
    sleep(1)
    
    type_writer("You hear the buzzing sound again. The Acrobat is speaking to you.")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"You've been drinking again haven't you?\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer(f"\"Typical {player_name}!\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"There are a couple of ways we can do this...\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"We can go with my idea.\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"I can use my stupendously amazing acrobatic skills to cleverly and cleanly work out a way in\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"Or...\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"We can go with the idiots idea...\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("The idiot The Acrobat is referring to is The Demolition Guy, a realitive newcomer to your inner circle.")
    # Wait for a second in between lines
    sleep(1)

    type_writer("The buzzing continues...")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"The idiot thinks we can blow our way through any obsticles... utterly barbaric\"")
    # Wait for a second in between lines
    sleep(1)

    type_writer("\"You need to make a decision... Which idea will it be?\"", BLUE)
    # Wait for a second in between lines
    sleep(1)

    type_writer("You indicate your decision by tapping one of your chips on one of the other chips on the table.")

    type_writer("The faint clicking sound should be picked up by your ear piece.")
    
    type_writer("Choose Option 1 to go with The Acrobat's plan or Option 2 to go with The Demolition Guy's plan", YELLOW)

    type_writer("\"If you can't decide you could always always flip a coin?\" Choose Option 3 to let fate decide", YELLOW)
    
    option = input()

    # Act on the users chosen option
    if option == "1":
        # Print Option 1 Outcome Text
        type_writer("You decide to go with The Acrobats plan.")
        sleep(1)
        type_writer("Press Enter To Continue...", BLUE)
        input()
        scene_3()
    
    elif option == "2":
        type_writer("You decide to go with The Demolition Guys plan")
        sleep(1)
        type_writer("Press Enter To Continue...", BLUE)
        input()
        scene_4()

    elif option == "3":
        # Choose a random number, either 0 or 1
        coin_toss = random.randint(0, 1)
        if coin_toss == 0:
            # Print Option Negative 2 Outcome Text
            type_writer("Fate decides that you will go with The Demolition Guy's plan.")
            sleep(1)
            type_writer("Press Enter To Continue...", BLUE)
            input()
            scene_4()
        elif coin_toss == 1:
            # # Print Option 2 Negative Outcome Text
            type_writer("Fate decides that you will go with The Acrobat's plan.")
            sleep(1)
            type_writer("Press Enter To Continue...", BLUE)
            input()
            scene_3()
        
    else:
        # Ask the user to try
        type_writer("Invalid Input. Please Press Enter To Try Again...", RED)
        input()
        # Start the current scene again by calling the current function
        scene_2()


# Scene 3
def scene_3():
    # Clear the terminal ready for the new scene
    global player_name
    global player_score
    clear()
    # Print scene text
    type_writer("The Acrobat arrives at the entrance to the back of house in the casino and finds two guards blocking her entry towards the location of the vault")
    # Wait for half a second in between lines
    sleep(1)
    
    type_writer("She radios through and asks you how she should proceed, giving you three options to chose from - will you pick the lucky number?")
    # Wait for half a second in between lines
    sleep(1)
    
    type_writer(f"\'{player_name} should I either....\'")
    # Wait for half a second in between lines
    sleep(1)

    # Print scene options
    type_writer("""
    1. Climb through the exposed AC vents to shimmy over guards to circumvent the door? 
    2. Or I could wear my disguise and slip past the guards dressed as maintainance?
    3. Although the easiest way would be to just us my skills to flip over them and hope they don't notice? """, YELLOW)
    # Wait for half a second in between lines
    sleep(1)

    # Record the users option
    type_writer("'Please Choose your hand sir 1, 2 or 3', states the dealer")
    option = input()

    # Act on the users chosen option
    if option.strip() == "1":
        # Print Option 1 Outcome Text
        type_writer("She climbs up into air conditioning vents stealthily and passes over the doorway but as she travels over the doorway the vent cover falls to the floor... ")
        sleep(1)
        
        type_writer("The falling vent cover creates such a noise the guards call on the radio for assistance")
        sleep(1)
        
        type_writer("A door opens below the Acrobat and a guard rushes out of the CCTV control room", GREEN)
        # add to total score
        player_score += 10
        type_writer("Press Enter To Continue...", BLUE)
        input()
        scene_5()
        
    elif option.strip() == "2":
        # Print Option 2 Outcome Text
        x=random.randint(1,5)
        if x > 3:
            type_writer("She skillfully slips into her disguise as a maintenance worker in the nearby phonebooth and swiftly makes for the entrance")
            sleep(1)             
            
            type_writer("The first guard clears her to walk through without batting an eyelid, although he did give her a flirtatious look")
            sleep(1)
              
            type_writer("She slips through the door flirting back as she passes both guards by, with a swing in her hips.")
            sleep(1)
              
            type_writer("She woos the male guards so much they radio through to their colleague in CCTV Control Room to come and check her out")
            sleep(1)
            
            type_writer("The Control Room Security launches out of his office and smooths by her to discuss with the boys, leaving his station open", GREEN)
    
            player_score += 10
            type_writer("Press Enter To Continue...", BLUE)
            input()
            scene_5() 
             
        else:
            type_writer("She skillfully slips into her disguise as a maintenance worker in the nearby phonebooth and swiftly makes for the entrance")
            sleep(1)    
        
              
            type_writer("The first guard clears her to walk through but the second says, 'Hold it there, where is your badge?'...", RED)
            sleep(1)
        
            type_writer("The Acrobat has to think fast, taking out the second guard with a chop around the neck whilst lunging into the groin of the unsuspecting first")
            sleep(1)
        
            type_writer("Both guards fall to the floor and the Acrobat takes a second swing at the first guard to knock him out also")
            sleep(1)
            
            type_writer("With both guards unconscious, she pulls out a couple of pillows from her Mary Poppins-esque bag and places them in a huddles sleeping position.")
            sleep(1)
        
            type_writer("The growns arouse the attention of the security in the CCTV Control Room, who then exits his station to check out the source of the noise.")
            type_writer("Press Enter To Continue...", BLUE)
            input()
            scene_5()
        
    elif option.strip() == "3":
        # Print Option 3 Outcome Text
        type_writer("The Acrobat runs and takes her leap of faith but faith was not enough and she falls upon the guards causing them momentary unconsciousness.", RED)
        sleep(1)
        
        type_writer("She slips past into the corridor and hides behind a trolley to case her next move, when suddenly, the first guard begins to grown.")
        sleep(1)
        
        type_writer("A door opens below the Acrobat and a guard rushes out of the CCTV control room")
        type_writer("Press Enter To Continue...", BLUE)
        
        # add to total score
        # call score check
        input()
        scene_5() 


# Scene 4
def scene_4():
    # Clear the terminal ready for the new scene
    global player_name
    global player_score
    clear()
    # Print scene text
    type_writer("The Demolition Guy arrives at the entrance to the back of house in the casino and finds two guards blocking his entry towards the location of the vault")
    # Wait for half a second in between lines
    sleep(1)
    
    type_writer("He radios through and asks you how he should proceed, giving you three options to chose from - will you pick the lucky number?")
    # Wait for half a second in between lines
    sleep(1)
    
    type_writer(f"\'{player_name} should I either....\'")
    # Wait for half a second in between lines
    sleep(1)

    # Print scene options
    type_writer("""
    1. Use a small explosive device to blow a hole in a nearby slot machine to create a distraction? 
    2. Or I could wear my disguise and slip past the guards dressed as maintainance?
    3. Although the easiest way would be to simply throw my small explosive device at their feet? """, YELLOW)
    # Wait for half a second in between lines
    sleep(1)

    # Record the users option
    type_writer("'Please Choose your hand sir 1, 2 or 3', states the dealer")
    option = input()

    # Act on the users chosen option
    if option.strip() == "1":
        # Print Option 1 Outcome Text
        type_writer("He smoothly moves across the floor to the nearest slot machine and places the ordinance near the coin dispenser... ")
        sleep(1)
        
        type_writer("In a ghost like fashion he moves back to a safe location and detonates the device.")
        sleep(1)
        
        type_writer("The explosion launches coins into the air and a crowd begins to gather. The guards run to the scene, leaving their post", GREEN)
        sleep(1)
        
        type_writer("The Demolition Man waits a moment and another guard comes rushing out to support his team members, leaving the door open")
        sleep(1)
            
        type_writer("Once running through the open door he notices the CCTV Control Room is also now empty...")
        # add to total score
        player_score += 10

        type_writer("Press Enter to Continue...", BLUE)
        input()
        scene_6()
        
    elif option.strip() == "2":
        # Print Option 2 Outcome Text
        x=random.randint(1,5)
        if x > 3:
            type_writer("He skillfully slips into his disguise as a maintenance worker in the nearby phonebooth and swiftly makes for the entrance")
            sleep(1)             
            
            type_writer("The first guard clears him to walk through, laughing about how his work is so much harder than just standing around watching all day")
            sleep(1)
              
            type_writer("He walks through the door laughing and says, 'Ahh but did you see that guy with the crowbar over there trying to crack the slot machine?'")
            sleep(1)
              
            type_writer("Both guards look shocked and call through to the CCTV Control Room to check the cameras, to no avail", GREEN)
            sleep(1)
            
            type_writer("The Control Room Security launches out of his office rushes over to the two guards the Demolition Guy has breezed past to discuss their options, leaving the CCTV Room open for action...")
            
            sleep(0.5)
            type_writer("Press Enter to Continue...", BLUE)
            player_score += 10
            input()
            scene_6() 
             
        else:
            type_writer("He skillfully slips into his disguise as a maintenance worker in the nearby phonebooth and swiftly makes for the entrance")
            sleep(1)    
        
              
            type_writer("The first guard clears him to walk through but the second says, 'Hold it there, where is your badge?'...", RED)
            sleep(1)
        
            type_writer("The Demolition Guy has to think fast, taking out the second guard with the butt of his rifle, he swings the rifle round to the first, who faints at the sight of it")
            sleep(1)
        
            type_writer("With both guards on the floor the Demo Guy pulls out a couple of inflatable pillows with a quick release air canister")
            sleep(1)
            
            type_writer("After inflating the pillows, he lays out the guards, huddled together in a sleeping position and the first guard begins a whimper .")
            sleep(1)
        
            type_writer("The unusual sounds arouse the attention of the security in the CCTV Control Room, who then exits his station to check out the source of the noise") 
            sleep(0.5)

            type_writer("Press Enter to Continue...", BLUE)
            input()
            scene_6()
        
    elif option.strip() == "3":
        # Print Option 3 Outcome Text
        type_writer("Taking the small explosive device out of his satchel, the Demolition Guy launches it in the direction of the guards but misses")
        sleep(1)
        
        type_writer("The device bounces off the door towards a nearby wall, exploding on contact and leaving a huge gaping hole.", RED)
        sleep(1)
        
        type_writer("Puzzled, the guards go to investigate the newly formed doorway into the blackjack arena.")
        sleep(1)
        
        type_writer("The Demo guy moves cautiously towards the entrance, only to be met with the door swinging open and another guard rushing by in a cold sweat.")
        sleep(1)
        
        type_writer("Seizing the opportunity, he jumps to the closing door to dive into the back of house, only to find the CCTV Control Room door was open and the room unattended...")
        sleep(0.5)
        type_writer("Press Enter to Continue...", BLUE)
        

        input()
        scene_6() 


# This function will be used in both scene 5 and scene 6 if the play decides to attempt to hack the camera control server
def hack_camera_server():
    attempt = random.randint(0, 1)

    if attempt == 1:
        return True
    else:
        return False


# Scene 5
def scene_5():
    # Clear the terminal ready for the new scene
    global player_name
    global player_score
    clear()
    # Print scene text
    type_writer("Sliding out from her hiding place behind the conveniently placed trolley, the Acrobat checks the lay of the land and notices the CCTV Control Room is still empty")
    # Wait for half a second in between lines
    sleep(1)
    
    type_writer("She radios through to you - the master planner - again for instructions on how to move forward. Little does she know you have forgotten the lot")
    # Wait for half a second in between lines
    sleep(1)
    
    type_writer(f"\'{player_name} I'm at the CCTV Control Room and cannot remember the plan, should I....\'")
    # Wait for half a second in between lines
    sleep(1)

    # Print scene options
    type_writer("""
    1. I could attempt hacking the server and disable all the cameras for the next 2 hours - giving us time to escape?
    2. Although I'd prefer to bounce from camera to camera spraying the lenses, using my skills to the max, to cover our tracks?
    3. If you insist on a third option I could enter the Control Room and unhook the cables to the server and power supply? 
    """, YELLOW)
    # Wait for half a second in between lines
    sleep(1)

    # Record the users option
    type_writer("Your attention is drawn back to the table as the dealer asks you again to choose your hand")
    option = input()

    # Act on the users chosen option
    if option.strip() == "1":
        attempt = hack_camera_server()
        if attempt == True:
       
            type_writer("After a suave shimmy into the CCTV Control Room, the disappointment hit her that she won't need to flash her talents in hear today")
            sleep(1)             
            
            type_writer("She drably takes the desk chair and hunkers down on the keys to begin her attempt to hack the system")
            sleep(1)
        
            type_writer("After a few key entry errors and some cautionary beeps the system starts to crank down, the hack is working.... ")
            sleep(1)
        
            type_writer("Each and every monitor in front of her switches off the display of the cameras they are assigned. It has worked, she simply cannot believe her luck.", GREEN)
            sleep(1)
            
            type_writer("Knowing that it worked perked her interest, maybe she could diversify in the future, become a hack as well - but she quickly realizes, there are more pressing issues at hand.")
            sleep(1)
        
            type_writer("On that thought, the Acrobat makes for the door, skunks down the corridor and eads to the Vault area .")
            
            player_score += 10
        
            type_writer("Press Enter to Continue...", BLUE)
            input()
            scene_7()
        
        else:
            type_writer("After a suave shimmy into the CCTV Control Room, the disappointment hit her that she won't need to flash her talents in hear today")
            sleep(1)             
            
            type_writer("She drably takes the desk chair and hunkers down on the keys to begin her attempt to hack the system")
            sleep(1)
        
            type_writer("As she is tapping away, the system seems to gear up, adding password request after password request - she is having a bad feeling about this")
            sleep(1)
        
            type_writer("After accidentally getting past a few of the requests using a few tricks a friend taught her, the Acrobat soon realizes that this just is not going to go her way", RED)
            sleep(1)
            
            type_writer("An alarm starts to go off, 'Is it local' she thinks to herself - no time to think she pulls out a usb the same friend mentioned gave to her and jams it into the main console.")
            sleep(1)
        
            type_writer("Eureka, the system shuts down - with a few sparks mind - and the alarms shut down. Hopefully she hasn't attracted too much attention.")      
            sleep(1)
            
            type_writer("With no time to waste, The acrobat dives out of the Control Room and rushes down the corridor towards the Vault Area, gasping for breath and fearful she might have blown the whole op.")
            
            type_writer("Press Enter to Continue...", BLUE)
            input()
            scene_7()
        
    elif option == "2":
       # Print Option 2 Outcome Text
        type_writer("So elated that she can use her skills the way she has been training for, she leaps up towards the first camera and sprays the lens without hesitation.")
        sleep(1)
        
        type_writer("Pouncing across the corridor without touching the floor she takes out the second, then the third and the fourth just seemed to be covered in a flash.")
        sleep(1)
        
        type_writer("Leaping towards the fifth, she stumbles, falls to the floor and her position is exposed - hoping she has gotten away with it, she scrambles to cover it but an alarm begins to ring.", RED)
        sleep(1)
        
        type_writer("Upon the sound of the alarm, she looks over her shoulder and sees the Control Room Guard heading in her direction. Another quick glance she notices a small vent in the wall.")
        sleep(1)
        
        type_writer("Launching herself in desperation, she makes it into the small ventilation space and notices it is a dead end - nothing to do but wait")
        sleep(1)
        
        type_writer("She spots the Control Room security guard pass by and knows all she can do is hang out, wait and hope she hasn't blown the op.")
        sleep(1)
        
        type_writer("Still waiting.")
        sleep(3)
        
        type_writer("Still waiting.")
        sleep(3)
        
        type_writer("Still waiting.")
        sleep(3)
        
        type_writer("Still waiting.")
        sleep(3)
        
        type_writer("Still waiting.")
        sleep(3)
        
        type_writer("Waiting over, finally, feeling dumb but also relieved that the op isn't completely blown, she skulks out of the vent and creeps down towards the Vault area")
        
        type_writer("Press Enter to Continue...", BLUE)
        input()
        scene_7()
            
    elif option.strip() == "3":
          # Print Option 3 Outcome Text
        type_writer("Moving with a flare that only an acrobat could, she rolls and tumbles into the Control Room ")
        sleep(1)
        
        type_writer("Once inside she begins to dance across the walls and behind each unit, unplugging the fibre optic and power connections ", GREEN)
        sleep(1)
        
        type_writer("Once she completed her dance, she smoothly slides out of Control Room and bounces down the corridor to the area where the Vault is located")
        # add to total score
        player_score += 10
        
        type_writer("Press Enter to Continue...", BLUE)
        input()
        scene_7()


# Scene 6
def scene_6():
    # Clear the terminal ready for the new scene
    global player_name
    global player_score
    clear()
    # Print scene text
    type_writer("With his hawk like eyes he cases the scene and  deduces his next move - 'Er, I must radio through to the boss' he thinks to himself")
    # Wait for half a second in between lines
    sleep(1)
    
    type_writer("He grabs the radio firmly, almost crushing it and asks...")
    # Wait for half a second in between lines
    sleep(1)
    
    type_writer(f"\'Boss, er, {player_name}, oops, you did say no names - er,  I'm at the CCTV Control Room and cannot remember the plan, should I....\'")
    # Wait for half a second in between lines
    sleep(1)

    # Print scene options
    type_writer("""
    1. Enter the Control Room and blow the whole place up? 
    2. Or I could attempt hacking the server and disable all the system till the end of the day - giving us time to escape?
    3. And maybe, it would be more fun for me to just blow up each camera along the way, that way they'll not fix 'em till next week hey? """, YELLOW)
    # Wait for half a second in between lines
    sleep(1)

    # Record the users option
    type_writer("Your attention is drawn back to the table as the dealer asks you again to choose your hand")
    sleep(1)
   
    option = input()

    # Act on the users chosen option
    if option.strip() == "1":
        # Print Option 1 Outcome Text
        type_writer("Totally buzzing as all Demo Peeps are, with explosives in hand, the Demo Guy rigs the entire Control Room to blow ")
        sleep(1)
        
        type_writer("Jumping out the room with all the finesse of an elephant, he takes cover and flicks the trigger to blow")
        sleep(1)
        
        type_writer("The detonation goes off without a hitch and the room becomes a hole in the ground - 'all the cameras are now off sir' he radio through to you", GREEN)
        sleep(1)
        
        type_writer("With the cameras out of action he waltzes down the hall to the Vault area without a care in the world")
        # add to total score
        player_score += 10
        type_writer("Press Enter to Continue...", BLUE)
        input()
        scene_8()
        
    elif option == "2":
        attempt = hack_camera_server()
        if attempt == True:
       
            type_writer("Blundering into the empty CCTV Control Room, the Demolition Guy reaches for a chair and takes a seat")
            sleep(1)             
            
            type_writer("The seat cracks under his weight but it doesn't phase him, so he cracks his knuckles in retaliation")
            sleep(1)
        
            type_writer("After a few key entry errors and some cautionary beeps the system starts to crank down, the hack is working.... ", GREEN)
            sleep(1)
        
            type_writer("Each and every monitor on the display ahead of him shows each camera powering down. 'It has worked boss, the cameras are offline'.")
            sleep(1)
            
            type_writer("Safe in the knowledge the cameras cannot catch him out he swans down the corridor to blow up the safe, entering the Vault area.")
            
            player_score += 10
            type_writer("Press Enter to Continue...", BLUE)
            input()
            scene_8()
        
        else:
            type_writer("Tripping a little on his way into the CCTV Control Room, the feeling that things aren't going his dawns on him")
            sleep(1)             
            
            type_writer("Grabbing the nearest seat and hunkering down, it cracks under his weight but it doesn't phase him, so he cracks his knuckles in an act of defiance")
            sleep(1)
        
            type_writer("Bashing away on the terminals keys, the system seems to gear up, adding password request after password request - the bad feeling grows", RED)
            sleep(1)
        
            type_writer("After accidentally getting past a few of the requests using a few tricks a friend had shown him, the Demo Guy soon realizes that this just is not going to go his way at all")
            sleep(1)
            
            type_writer("An alarm starts to go off, 'Is it local' he thinks to himself - no time to think he pulls out a usb from the same friend mentioned and jams it into the main console.")
            sleep(1)
        
            type_writer("Booya! The system shuts down - with a few sparks, giving him a buzz - and the alarms all shut down.")      
            sleep(1)
            
            type_writer("Not concerned too much, he climbs out of the seat - breaking it some more - and swaggers down towards the Vault area with his rifle armed and ready - just in case.")
            sleep(1)
            type_writer("Press Enter to Continue...", BLUE)
            input()
            scene_8()
            
    elif option.strip() == "3":
        # Print Option 3 Outcome Text
        type_writer("Diggin' the decision - although a little sceptical that it was the one in the final plan - the Demo Guy chucks an ordinance at the first camera in his way.")
        sleep(1)
        
        type_writer("Pounding the corridor with confidence, he takes out the second, then the third and the fourth just went up with an electrifying bang.")
        sleep(1)
        
        type_writer("Now at the fifth camera, the detonation device fails, the mini explosives aren't working, so he grabs his rifle and takes a shot to trigger the device and misses.", RED)
        sleep(1)
        
        type_writer("The gun fire attracts the attention of the Control Room Guard who was already suspicious due to the cameras seemingly switching off.")
        sleep(1)
        
        type_writer("The guard proceeds to head the Demolition Guys way down the corridor - so he rushes towards to him with butt of his rifle, knocking the guard to the deck")
        sleep(1)
        
        type_writer("He notices a vent to side of him, cracks it open and to his luck, there is space for a body, so he bundles the guard inside and hopes for the best")
        sleep(1)

        type_writer("Laughing at the close call, The Demo Guy swans down the corridor to the Vault are without a care in the world. Well, apart from the thought 'Hope the boss doesn't find out about this'")
        # add to total score
        # call score check
        type_writer("Press Enter to Continue...", BLUE)
        input()
        scene_8() 

# Scene 7
def scene_7():
    # Clear the terminal ready for the new scene
    global combination_tried
    global player_score
    clear()
    # Print scene text
    type_writer("The Acrobat finally arrives at the Vault, the reason you are all here.")
    # Wait for half a second in between lines
    sleep(1)
    type_writer("At least you imagine so, you're still a little unsure.")
    sleep(1)
    type_writer("The vault in question is a large metal door with a control panel on the front. There is, however, a ventilation duct")
    type_writer("a short way down the hall, that it looks like the Acrobat could fit through and that probably leads to the vault.")
    sleep(0.5)
    type_writer(f"\"what's the plan then {player_name}? How are we getting in to this thing?\" \"Should I...\"")

    # Print scene options
    type_writer(
        """
    1. Get inside through the vents and try to unlock the vault from the inside?
    2. Try to guess the combination to the vault?
    3. Get inside through the vents and try to retrieve the money and bring it back through the vents? """, YELLOW)
    
    # Wait for half a second in between lines
    sleep(0.5)

    # Record the users option
    type_writer("Please Choose Option 1, 2 or 3")
    option = input()

    # Act on the users chosen option
    if option.strip() == "1":
        # Print Option 1 Outcome Text
        type_writer("You cough once.")
        sleep(0.5)
        type_writer("\"You got it.\" she says and starts climbing, seemingly effortlessly, into the vent.")
        sleep(0.5)
        type_writer("You wait impatiently for what feels like an eternity.")
        sleep(1)
        type_writer("\"Aaand done.\" she says through you earpiece. Suddenly the vault doors whir into life and the vault springs open.", GREEN)
        sleep(0.5)
        type_writer("\"What? Did you doubt me?\"")
        sleep(0.5)
        type_writer("She starts packing money into her bag, when a wall in the hallway explodes outwards and out walks the Demo Guy.")
        sleep(0.5)
        type_writer("\"Got our escape route sorted!\" he says and starts helping her pack the money into two more bags.")
        sleep(0.5)
        type_writer("They start making their escape through the newly made opening. You also start making your way to the exit to regroup.")
        # add to total score
        player_score += 10
        sleep(1)
        type_writer("Press Enter To Continue...", BLUE)
        input()
        end_game_chance()
    elif option.strip() == "2":
        # Print Option 2 Outcome Text
        if combination_tried == False:
            x = random.randint(1, 5)
            type_writer("You cough twice.")
            sleep(0.5)
            type_writer("\"Wait, seriously? I was joking.\" She laughs, approaching the control panel on the door.")
            sleep(0.5)
            type_writer("You pick up a chip from the table in front of you and start tapping it against another, loud enough that the Acrobat can hear, and start tapping the\nfirst number that comes into your head.")
            sleep(1)
            if x > 3:
                type_writer("Somehow, through an extraordinary feat of luck, you manage to completely guess the combination to the vault.", GREEN)
                sleep(0.5)
                type_writer("\"Huh... Well you kept that knowledge quiet.\" She says, obviously assuming that you actually knew what you were doing.")
                sleep(0.5)
                type_writer("The door starts to open and she begins packing money into her bag, moments later a wall in the hallway explodes outwards and out walks the Demo Guy.")
                sleep(0.5)
                type_writer("\"Got our escape route sorted!\" he says and starts helping to pack the money into two more bags.")
                sleep(0.5)
                type_writer("They start making their escape through the newly made opening. You also start making your way to the exit to regroup.")
                # add to total score
                player_score += 10
                sleep(1)
                type_writer("Press Enter To Continue...", BLUE)
                input()
                end_game_chance()
            else:
                type_writer(
                    "You did not manage to 'guess' the combination to the vault and are now locked out from further guesses.", RED
                )
                sleep(2)
                type_writer(
                    "You're honestly not sure why you thought you could do so."
                )
                sleep(1)
                type_writer("\"Well that went as expected...\"")
                type_writer("Press Enter to return to the options.")
                input()
                combination_tried = True
                scene_7()
        else:
            type_writer(
                "She inspects the control panel. She is still locked out of trying further combinations. You will have to choose another plan.", RED
            )
            sleep(0.5)
            type_writer("Press Enter to return to options.")
            input()
            scene_7()
    elif option.strip() == "3":
        # Print Option 3 Outcome Text
        type_writer("You cough three times.")
        sleep(0.5)
        type_writer("\"You got it.\" she says and starts climbing, seemingly effortlessly, into the vent.")
        sleep(0.5)
        type_writer("You wait impatiently for what feels like an eternity.")
        sleep(1)
        type_writer("Finally she chimes in \"Alright, we're in business.\"")
        sleep(0.5)
        type_writer("She starts to shuttle bags of cash back and forth, managing a couple of trips.")
        sleep(0.5)
        type_writer("However, suddenly there is a loud creaking sound and then the vent she has been using crashes down within the vault, leaving her trapped inside.", RED)
        sleep(1)
        type_writer("\"Guys, we've got an issue, I'm trapped in the vault.\"")
        sleep(0.5)
        type_writer("While you are panicking, wondering how to proceed, the wall in the hallway outside the vault violently explodes outwards and out walks the Demo Guy.")
        sleep(0.5)
        type_writer("\"Got our escape route sorted!\" he says, \"Wait, where are you?\" \"I'm stuck in the vault, I think you've got to just bail!\" replies the Acrobat.")
        sleep(0.5)
        type_writer("He doesn't take much convincing and grabs the two bags she managed to retrieve so far and heads for the exit. You start making your way to the exit to regroup.")
        sleep(0.5)
        type_writer("Press Enter To Continue...", BLUE)
        input()
        # Call end 2
        end_2()
    else:
        # Ask the user to try
        type_writer("Incorrect Input. Please Press Enter Try Again...", RED)
        input()
        # Start the current scene again by calling the current function
        scene_7()


# Scene 8
def scene_8():
    # Clear the terminal ready for the new scene
    global combination_tried
    global player_score
    clear()
    # Print scene text
    type_writer("The Demolition Guy finally arrives at the Vault, the reason you are all here.")
    # Wait for half a second in between lines
    sleep(1)
    type_writer("At least you imagine so, you're still a little unsure.")
    sleep(1)
    type_writer("The vault in question is a large metal door with a control panel on the front.")
    sleep(0.5)
    type_writer("\"Alright then, how are we cracking this thing open?\" asks the Demolition Guy")
    sleep(0.5)
    type_writer("\"Should I...\"")
    # Print scene options
    type_writer(
        """
    1. Try to open the vault by planting an explosive directly on the lock?
    2. Try to guess the combination to the vault?
    3. Try to open the vault by planting explosives on the hinges of the door? """, YELLOW)
    # Wait for half a second in between lines
    sleep(0.5)

    # Record the users option
    type_writer("Please Choose Option 1, 2 or 3")
    option = input()

    # Act on the users chosen option
    if option.strip() == "1":
        # Print Option 1 Outcome Text
        type_writer("You cough once.")
        sleep(0.5)
        type_writer("The Demolition Guy plants and explosive straight on the lock and retreats to a safe distance, hiding around the corner of the hallway.")
        sleep(0.5)
        type_writer("After a loud bang and a lot of smoke, he cautiously returns to the vault door.")
        sleep(0.5)
        type_writer("The Demo Guy gives the door a light push and it slowly swings open. \"Worked like a charm.\"", GREEN)
        sleep(0.5)
        type_writer("He starts to shovel money into his bag. As he is doing so, he hears some thuds from the ceiling outside.")
        sleep(0.5)
        type_writer("One of the ceiling tiles falls to the ground and a familiar face appears from above. \"Got our exit route planned!\" says the Acrobat.")
        sleep(0.5)
        type_writer("She starts helping to load the bags of money, and then helps him into the hole in the ceiling and they both start heading for the exit.")
        sleep(0.5)
        type_writer("You also start heading to the nearest exit to regroup with the others.")
        # add to total score
        player_score += 10
        end_game_chance()
    elif option.strip() == "2":
        # Print Option 2 Outcome Text
        if combination_tried == False:
            x = random.randint(1, 5)
            type_writer("You cough twice.")
            sleep(0.5)
            type_writer("\"Wait, are you serious?\" asks the Demo Guy. He approaches the control panel.")
            sleep(0.5)
            type_writer("You pick up a chip from the table in front of you and start tapping it against another, loud enough that the Demo Guy can hear, and start tapping the\nfirst number that comes into your head.")
            sleep(1)
            if x > 3:
                type_writer("Somehow, through an extraordinary feat of luck, you manage to completely guess the combination to the vault.", GREEN)
                sleep(0.5)
                type_writer("\"You're kidding me. Did you know that the whole time?\" He says, obviously assuming that you actually knew what you were doing.")
                sleep(0.5)
                type_writer("Together you start to shovel money into bags. As you are doing so, you hear some thuds from the ceiling outside.")
                sleep(0.5)
                type_writer("One of the ceiling tiles falls to the ground and a familiar face appears from above. \"Got our exit route planned!\" says the Acrobat.")
                sleep(0.5)
                type_writer("She starts helping to load the bags of money, and then helps him into the hole in the ceiling. They both start heading for the exit and you do the same.")
                # add to total score
                player_score += 10
                sleep(1)
                type_writer("Press Enter To Continue...", BLUE)
                input()
                end_game_chance()
            else:
                type_writer("You did not manage to 'guess' the combination to the vault and are now locked out from further guesses.", RED)
                sleep(2)
                type_writer("You're honestly not sure why you thought you could do so.")
                sleep(1)
                type_writer("Press Enter to return to options.")
                input()
                combination_tried = True
                scene_7()
        else:
            type_writer("You inspect the control panel. You are still locked out of trying further combinations. You will have to choose another plan.", RED)
            type_writer("Press Enter to return to the options.", BLUE)
            input()
            scene_7()
    elif option.strip() == "3":
        # Print Option 3 Outcome Text
        type_writer("The Demolition Guy plants a couple of explosives on each hinge of the door and retreats to a safe distance, hiding around the corner of the hallway.")
        sleep(0.5)
        type_writer("After a loud bang and a lot of smoke he returns to the vault door to find it seemingly unharmed.")
        sleep(0.5)
        type_writer("\"Well, that didn't work great.\"")
        sleep(1)
        type_writer("However as the Demolition guy starts inspecting the door more closely it begins to slowly tilt in his direction.")
        sleep(0.5)
        type_writer("It crashes down, trapping his leg underneath the weight of the door.", RED)
        sleep(1)
        type_writer("A few moments later there is a banging sound from above.")
        sleep(0.5)
        type_writer("One of the ceiling tiles falls to the ground and a familiar face appears from above. \"Got our exit route planned!\" says the Acrobat. \"Woah, what happened here?\"")
        sleep(0.5)
        type_writer("\"I'm stuck! you gotta help me out!\"")
        sleep(0.5)
        type_writer(f"\"Sorry man, there's no time. {player_name}, Time to regroup.\"")
        sleep(0.5)
        type_writer("The Acrobat starts packing their 2 bags and makes their way back into the ceiling to escape. You also start heading for the door to regroup.")
        # Call end 4
        sleep(1)
        type_writer("Press Enter To Continue...", BLUE)
        input()
        end_4()
    else:
        # Ask the user to try
        type_writer("Incorrect Input. Please Press Enter Try Again...", RED)
        input()
        # Start the current scene again by calling the current function
        scene_8()


# End game chance function
def end_game_chance():
    global player_score
    # grabs the player score, which is decided by correct choices throughout the game.
    chance = random.randint(1, 20)
    # creating a random number between 1 and 20. Depending on the players total score it is then decided how high this random number needs to be to be considered successful.
    if player_score == 30:
        # If score is 40 then the player has won, no random chance is decided as this is the perfect score.
        # call End 1
        end_1()
    elif player_score == 20:
        # If score is 20 then the 'chance' needs to be higher than 5. This is quite likely but presents a chance of failure.
        if chance > 5:
            # call End 1
            end_1()
        else:
            # call End 3
            end_3()
    elif player_score == 10:
        # If score is 10 then the 'chance' needs to be higher than 15. This is very difficult.
        if chance > 15:
            # call End 1
            end_1()
        else:
            # call End 3
            end_3()
    else:
        # If the player score is 0 then they have lost and will always get caught.
        # call End 3
        end_3()


# Takes a score as input and then it returns a string containing the players score as a dollar value
def money_score(score):
    # Multiply the score by 1 million
    money_score = score * 1000000

    # Add a small amount of randomness to the score for flavour
    money_score = money_score * random.uniform(0.9775894, 1.1534645)

    # Round the player money to 2 decimal places so it looks like real money value
    money_score = round(money_score, 2)

    # Print out the players score
    return f"${money_score}"


def end_1():
    global player_score
    type_writer(f"You manage to regroup with the whole group. You successfully flee from the casino with {money_score(player_score)}", GREEN)
    sleep(1)
    type_writer("Well Done!", GREEN)
    sleep(1)
    type_writer("Press Enter to Exit the Game...", BLUE)
    input()


def end_2():
    global player_score
    type_writer(f"You regroup with The Demolition Guy. You could have escaped with {money_score(player_score)}...", YELLOW)
    sleep(1)
    type_writer(f"However The Acrobat got caught so you flee with {money_score(player_score * .66666)}", YELLOW)
    sleep(1)
    type_writer("Press Enter to Exit the Game...", BLUE)
    input()


def end_3():
    global player_score
    type_writer("You were too clumsy. You all get caught. All of the money you tried to steal still belongs to the casino", RED)
    sleep(1)
    type_writer("The Demolition Guy and The Acrobat both complain as you're all shoved put into the back of a van", RED)
    sleep(1)
    type_writer("Press Enter to Exit the Game...", BLUE)
    input()


def end_4():
    global player_score
    type_writer(f"You could have escaped with {money_score(player_score)}...", YELLOW)
    sleep(1)
    type_writer(f"However The Demolition Guy got caught so you get {money_score(player_score * .66666)}", YELLOW)
    sleep(1)
    type_writer("Press Enter to Exit the Game...", BLUE)
    input()


# Start the game. This needs to happen right at the end
game_start()