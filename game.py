#!/usr/bin/python3
import time
from random import randint

from map import rooms
from player import *
from items import *
from gameparser import *
from people import *
from updater import *


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it in the format
    shown in the doctest below.

    >>> print_inventory_items([item_goldgoblet, item_goblet, item_oldboot, item_knife])
    You have a chalice, along with a goblet, a boot and a knife.

    >>> print_inventory_items([item_goldgoblet, item_goblet, item_oldboot])
    You have a chalice, along with a goblet and a boot.

    >>> print_inventory_items([item_goldgoblet])
    You have a chalice.

    """

    inv_str = ""    # concatenated string
    inv_count = 0   # number of inventory items

    for i in items :
        inv_count += 1

        if inv_count == 1 :
            # start of sentence
            inv_str += "You have " + i["name"]

        elif inv_count == 2 :
            # connector phrase to additional item
            inv_str += ", along with " + i["name"]
             
        else :
            # from this point, all other items are separated with commas
            inv_str += ", " + i["name"]
         

    if inv_str != "" :
        if inv_count <= 2 :
            # end sentence with full stop
            inv_str += "."

        else :
            # for items separated by commas, an 'and' is inserted before the last item for fluid reading
            inv_str = inv_str.rpartition(",")[0] + " and" + inv_str.rpartition(",")[2] + "."

        print(inv_str)
 
    else :
        print("You currently have no items.")
        


def print_exit(direction, leads_to):
    """Prints available exits in full sentences in one of three randomly-chosen formats.

    For example:
    The (place) lies to the (direction).      -or-
    To the (direction) is the (place).        -or-
    There is a (place) to the (direction).

    The Battlements is the only plural room name. Therefore, the following format is used:
    The battlements are to the (direction).

    """
    #needs to be reduxed 
    if leads_to.lower() == "battlements" :
        # special case for battlements room (see documentation)
        return "The " + leads_to.lower() + " are to the " + direction + ". "

    else :
        # choose one of three formats
        sentence_choice = randint(1, 3)

        if sentence_choice == 1 :
            return "The " + leads_to.lower() + " lies to the " + direction + ".\n"

        elif sentence_choice == 2 :
            return "To the " + direction + " is the " + leads_to.lower() + ".\n"

        elif sentence_choice == 3 :
            return "There is a " + leads_to.lower() + " to the " + direction + ".\n"



def print_people(people):
    """This function takes a list of people in the current room and displays it in the format
    shown in the doctest below.

    >>> print_people(['lady'])
    In the room, Catherine is present.

    >>> print_people(['lady', 'catherine'])
    In the room, Catherine is present.

    """

    ppl_str = ""    # concatenated string
    ppl_count = 0   # number of people in room
    
    for i in people :

        if not i.lower() in ppl_str.lower() :
            ppl_count += 1
            
            if ppl_count == 1 :
                # start of sentence
                ppl_str += "In the room, " + current_room["people"][i]["name"]
                
            else :
                # from this point, all other items are separated with commas
                ppl_str += ", " + current_room["people"][i]["name"]
                

    if ppl_str != "" :
        
        if ppl_count != 1 :
            # for items separated by commas, an 'and' is inserted before the last item for fluid reading
            ppl_str = ppl_str.rpartition(",")[0] + " and" + ppl_str.rpartition(",")[2] + " are present."

        else :
            # end sentence with full stop
            ppl_str += " is present."
            
        print(ppl_str)
        
    

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in the following format...

    _____________                  _______________

    ~ COURTYARD ~       -or-       ~ BATTLEMENTS ~
    _____________                  _______________
    
    ... where the underscores match the length of the room name.
    Other details such as the description of the room are printed afterwards.

    """
    
    # Display room name
    print("_" * (len(room["name"]) + 4))
    print()
    print("~ " + room["name"].upper() + " ~")
    print("_" * (len(room["name"]) + 4))
    
    # Display room description
    print()
    print(room["description"])
    print()

    # Print exits in full sentences
    exit_str = ""
    
    # Iterate over available exits
    for direction in room["exits"]:
        # Print the exit name and where it leads to
        exit_str += print_exit(direction, exit_leads_to(room["exits"], direction))

    if exit_str != "" :
        # Print the string
        print(exit_str)

        

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Courtyard"]["exits"], "south")
    'Battlements'
    >>> exit_leads_to(rooms["Throne Room"]["exits"], "east")
    'Great Hall'

    """
    
    return rooms[exits[direction]]["name"]



def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Courtyard"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Throne Room"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Great Hall"]["exits"], "north")
    True
    >>> is_valid_exit(rooms["Anteroom"]["exits"], "south")
    True
    """
    
    return chosen_exit in exits



def is_valid_person(people, chosen_person):
    """This function checks the chosen person is in the room.

    >>> is_valid_person(rooms["Throne Room"]["people"], "king")
    True
    >>> is_valid_person(rooms["Throne Room"]["people"], "lady")
    False
    
    """

    return chosen_person in people



def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room
    
    if is_valid_exit(current_room["exits"], direction) :
        current_room = move(current_room["exits"], direction)
        return True

    else :
        print("You cannot go there.")
        return False



def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    found_item = False
    
    for i in current_room["items"] :
        
        if i["id"] == item_id :
            inventory.append(i)
            current_room["items"].remove(i)

            print("You now possess the " + item_id + ".")
            print()
            time.sleep(0.5)

            found_item = True
            if item_id in item_room_descriptions:
                current_room["description"] = item_room_descriptions[item_id]
            break

        
    if found_item == False :
        print("You cannot take that.")  


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    found_item = False
    
    for i in inventory :
        if i["id"] == item_id :
            current_room["items"].append(i)
            inventory.remove(i)

            print("You no longer hold the " + item_id + ".")
            print()
            time.sleep(0.5)

            found_item = True
            break
        
    if found_item == False :
        print("You cannot drop that.")    



def execute_talk(people_id):
    """This function takes a people_id as an argument and begins a conversation
    with the person."""
    
    if is_valid_person(current_room["people"], people_id) :
        person_conv = current_room["people"][people_id]["conversation"]

        print(person_conv["opening"])
        input("Press ENTER to continue...")
        
        print("\nYou can ask...")
        qcount = 0

        if not person_conv["questions"] == [] :
            
            for q in range(0, len(person_conv["questions"])) :
                print("Input %d to ask '%s'" % (q+1, person_conv["questions"][q]))
                qcount += 1

            while True :
                try :
                    qask = int(input("\n> "))

                    if qask <= qcount and qask > 0 :
                        print(person_conv["responses"][qask-1])
                        input("Press ENTER to continue...")
                        break

                    else :
                        print("You cannot ask that.")

                except :
                    print("Type a number from the list of questions.")
        
    else :
        print("This person isn't here.")


def execute_play(puzzle):

    if puzzle in puzzles:
        
        if puzzles[puzzle] in current_room["puzzles"]:
            puzzles[puzzle]()
        else:
            print("You cannot play that here.")
    else:
        print("That is not a game.")

    

def execute_use(item_id, object_id):
	"""Check if item is in inventory
	check if object is in room
	run interaction code
	"""
	
	found_item = False
	found_object = False
	a = None
	b = None
	for i in inventory :
		if i["id"] == item_id :
			found_item = True
			a = i
		if i["id"] == object_id :
			found_object = True
			b = i
	for i in current_room["objects"]:
		if i["id"] == object_id:
			found_object = True
			b = i
	if found_item == True and found_object == True:
		if b["interaction"] != None:
			funct_run = b["interaction"]
			funct_run(item_id,object_id)
		else:
			print("Nothing interesting happens.")
	else:
		print("You cannot do that")
			
def execute_examine(object):
	"""Check if object is in inventory/room
	and return 'description' from the objects properties
	"""
	
	found_object = False
	a = None
	for i in inventory :
		if i["id"] == object:
			found_object = True
			a = i
	if found_object == False:
		for i in current_room["objects"]:
			if i["id"] == object:
				found_object = True
				a = i
	if found_object:
		print(a["description"])
		
	else:
		print("You cannot do that.")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command), executes the relevant function, supplying the second word
    as the argument.

    Note: This function will only return False when the player changes room.
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            if execute_go(command[1]) :
                return False      
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "talk":
        if len(command) > 1:
            execute_talk(command[1])
        else:
            print("Talk to whom?")
            
    elif command[0] == "play" or command[0] == "answer" or command[0] == "adjust":
        if len(command) > 1:
            execute_play(command[1])
        else:
            print("Play what?")
     
    elif command[0] == "use":
        if len(command) > 2:
            execute_use(command[1], command[2])
        else:
            print("You cannot do that.")
			
    elif command[0] == "examine":
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("Examine what?")
    else:
        print("This makes no sense.")



def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    print()
    print("What do you want to do?")

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input



def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Courtyard"]["exits"], "south") == rooms["Battlements"]
    True
    >>> move(rooms["Great Hall"]["exits"], "west") == rooms["Courtyard"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]

def main_menu():
	# This is the entry point of our program
	print("""                                                                                                     
     ##### ##                                /                                      /                
  ######  /##   #                          #/                    #                #/                 
 /#   /  / ##  ###                   #     ##                   ###               ##           #     
/    /  /  ##   #                   ##     ##                    #                ##          ##     
    /  /   /                        ##     ##                                     ##          ##     
   ## ##  /   ###   ###  /###     ######## ##  /## ###  /###   ###       /###     ##  /##   ######## 
   ## ## /     ###   ###/ #### / ########  ## / ### ###/ #### / ###     /  ###  / ## / ### ########  
   ## ##/       ##    ##   ###/     ##     ##/   ### ##   ###/   ##    /    ###/  ##/   ###   ##     
   ## ## ###    ##    ##            ##     ##     ## ##          ##   ##     ##   ##     ##   ##     
   ## ##   ###  ##    ##            ##     ##     ## ##          ##   ##     ##   ##     ##   ##     
   #  ##     ## ##    ##            ##     ##     ## ##          ##   ##     ##   ##     ##   ##     
      /      ## ##    ##            ##     ##     ## ##          ##   ##     ##   ##     ##   ##     
  /##/     ###  ##    ##            ##     ##     ## ##          ##   ##     ##   ##     ##   ##     
 /  ########    ### / ###           ##     ##     ## ###         ### / ########   ##     ##   ##     
/     ####       ##/   ###           ##     ##    ##  ###         ##/    ### ###   ##    ##    ##    
#                                                 /                           ###        /           
 ##                                              /                      ####   ###      /            
                                                /                     /######  /#      /             
                                               /                     /     ###/       /              """)
											   
	input("\n\n\n\t\t\t\t\tPress ENTER to play")
	opening()

def opening():
	print("""\n\nThis story begins in a small town outside of the grand castle Otterberg.
You have lived in the town all of your life, managing to get an education from the
your foster-father. One day he comes to you with a letter. He doesn't tell you who it
is from, he just says to read it:
	
------------------------------------------------------------------------------------------------	
"My beloved son

Hopefully, you will never have to read this letter but if you are reading this, 
it means something sinister has happened to us.

Don’t blame us for sending you away, our priority was to keep you safe.

Don’t try to claim it outright, but if you find yourself drawn to your birthright, seek out Gaius
in the castle Otterberg.

I know you will be brave, remember we love you no matter what.

Your mother" 
------------------------------------------------------------------------------------------------

You are left lost for words as your foster-father explains to you that you are really the son of
the recently deceased king and the true heir to the throne. 

You have an unquenchable urge for answers. He gives you a small amount of gold and sends you on 
your way to the castle.

To have regular access to the castle and to find Gaius you must have a job there. You bide your time
and manage to get yourself a job as a clerk looking after the gold of the kingdom. The new king
Wattus Rex was said to be impressed with your level of education and thought you would be a
great asset to the kingdom.

The time has now come to claim your birthright...""")
	input("\nPress ENTER to continue...\n")
	main()

def main():
    time.sleep(1)
    
    # Main game loop
    while True:
        from player import inventory
        global inventory
        if item_poison in inventory:
            print("Now you must decide, who will you use the poison on?")
            print("1. The King")
            print("2. The Viceroy")
            print("3. Catherine")
            ans = input("PICK A NUMBER ---->")
            if ans == "1":
                print("""You pour the poison into the king's drink as he is not looking.
He takes a sip and immediately his eyes open wide, head goes back and he hits the floor dead. This is some poison.

The viceroy stands up and immediately shouts:
"YOU! I knew you were trouble from day one clerk!, prepare to die!"

You quickly grab the sword from the nearby soldier's scabbard...


FINAL FIGHT - TYPE THE NUMBER THAT FLASHES ON SCREEN TO DEAL DAMAGE
""")
                input("PRESS ENTER TO FIGHT")
                from fightGame import fight
                player = {
                "id":"player",
                "name":"You",
                "health": 100.00} 

                computer = {
                "id":"computer",
                "name":"Viceroy",
                "health":100.00
}
                time.sleep(100)
                inventory = []
                quit()
            elif ans == "2":
                print("""You pour the poison into the viceroy's drink as he is not looking.
He is about to take a sip from his goblet... but quickly stops, sniffs the contents...

"POISON!"

"It was you wasn't it clerk! Throw him in the dungeon and make sure he never leaves!"

You are thrown into a disgusting dungeon cell. You live the remainder of your very short life in here, making friends with the rats.

GAME OVER
""")
                time.sleep(30)
                quit()

            elif ans == "3":
                print ("""You pour the poison into the lady's drink as she is not looking.
A guard notices what you have just done and charges you with his sword drawn!

Your head flies off in an arc right onto the main meal platter
At least you managed to ruin their banquet!

GAME OVER
""")
                time.sleep(30)
                quit()
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_people(current_room["people"])

        while True :
            # Execute the player's command and only repeat the above few lines of
            # code if the function returns True (see function documentation for more)
            print_inventory_items(inventory)
            print()
            command = menu(current_room["exits"], current_room["items"], inventory)
			
            
            if execute_command(command) == False :
                break
        

# If running as script, run main()
if __name__ == "__main__":
    main_menu()

