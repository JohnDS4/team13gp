

import random
def dice_game(): 
    """Plays a game of dice, using code from:
    https://code.sololearn.com/cjQ6V2Aj2rJk/#py
    by user PacketStorm, accessed 22/10/2018
    """
    
    def cee_lo_player():
        combo = roll()
        win = [4,5,6]
        loss = [1,2,3]
        w=9
        l=0
        print("You rolled %s" %combo[0] + "-%s" %combo[1] + "-%s" %combo[2])
        if combo==win:
            print("You rolled Cee-lo!")
            return w
        elif combo==loss:
            print("You rolled 123!")
            return l
        elif combo[0]==combo[1]==combo[2]:
            print("You rolled TRIP %s's!" %combo[0])
            return combo[0]
        elif combo[0]==combo[1] or combo[1]==combo[2]:
            if combo[0]==combo[1]:
                print("You rolled a PAIR of %s's!" %combo[1])
                print("Your number is %s!" %combo[2])
                return combo[2]
            elif combo[1]==combo[2]:
                print("You rolled a PAIR of %s's!" %combo[1])
                print("Your number is %s!" %combo[0])
                return combo[0]
        else:
            return cee_lo_player()


    def cee_lo_Soldier():
        combo = roll()
        win = [4,5,6]
        loss = [1,2,3]
        w=9
        l=0
        print("Soldier rolled %s" %combo[0] + "-%s" %combo[1] + "-%s" %combo[2])
        if combo==win:
            print("Soldier rolled Cee-lo!")
            return w
        elif combo==loss:
            print("Soldier rolled 123!")
            return l
        elif combo[0]==combo[1]==combo[2]:
            print("Soldier rolled TRIP %s's!" %combo[0])
            return combo[0]
        elif combo[0]==combo[1] or combo[1]==combo[2]:
            if combo[0]==combo[1]:
                print("Soldier rolled a PAIR of %s's!" %combo[1])
                print("Soldier number is %s!" %combo[2])
                return combo[2]
            elif combo[1]==combo[2]:
                print("Soldier rolled a PAIR of %s's!" %combo[1])
                print("Soldier number is %s!" %combo[0])
                return combo[0]
        else:
            return cee_lo_Soldier()

    def roll():
        dice1 = random.randrange(1,7,1)
        dice2 = random.randrange(1,7,1)
        dice3 = random.randrange(1,7,1)
        combo = [dice1,dice2,dice3]
        return sorted(combo)

    print("Rollin' the dice...\n")
    player = cee_lo_player()
    print("")
    Soldier = cee_lo_Soldier()
    print("")
    print("You: %s" %player)
    print("Soldier: %s" %Soldier)
    if player > Soldier:
        print("YOU WIN!")
        from player import inventory
        from items import item_money
        if item_money not in inventory:
            inventory.append(item_money)
            print("Soldier: 'Here take my gold.''")
    elif Soldier > player:
        print("YOU LOSE!")
    elif player == Soldier:
        print("DRAW!")



def riddle_lady():
    """A riddle is given and the player must answer correctly to progress"""
    from player import inventory
    from items import item_ingredients
    global inventory
    if item_ingredients not in inventory:
            print("Are you ready to answer my riddle?")
            print("'What's black when you buy it, red when you use it and white when you throw it away?'")
            ans = input('> ')
            if ans == "":
                return
            from gameparser import normalise_input
            ans2 = normalise_input(ans)
            if ans2[0] == "coal" or ans2[0] == "charcoal":
                    print("CORRECT!")
                    print("""\"I wanted to test you, to see if you were worthy.
    Here are some ingredients for a hangover cure. You'll definitely find this useful.
    They need to be mixed with water, so you'll need to find something else to contain it.\"\n""")
                    from player import inventory
                    from items import item_ingredients
                    from conversations import conv_lady
                    conv_lady["opening"] = """Leave me be now clerk. I've helped you more than I should."""
                    conv_lady["questions"] = ["But..."]
                    conv_lady["responses"] = ["(The lady turns away from you, she clearly doesn't want to talk)"]
                    inventory.append(item_ingredients)
                    from game import print_inventory_items
                    
            else:
                    print("WRONG! Try again.")
    


def dial_game():
    if input("What code do you want to enter into the dial?\n--->").lower() == "axgbyf":
        print("the dial makes a sharp click and the painting slides back to reveal a hole")
        print("the hole holds the 'Timeturner'")
        print("the door closes behind you and you are locked in the room")

        from map import room_ante
        from items import item_time_turner, object_wizard
        room_ante["exits"] = {}
        room_ante["items"].append(item_time_turner)
        room_ante["objects"] = [object_wizard]
        room_ante["puzzles"] = []
        room_ante["people"] = {}



puzzles = {"dice":dice_game, "riddle":riddle_lady, "dial": dial_game}
