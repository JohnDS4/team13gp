from updater import *

item_goldgoblet = {
    "id": "chalice",

    "name": "a chalice",

    "description":
        """A Golden Goblet *TODO-- """,

    "mass": 0,

    "interaction": None
}

item_goblet = {
    "id": "goblet",

    "name": "a goblet",

    "description":
        "A standard wooden goblet.",

    "mass": 0,

    "interaction": None
}

item_knife = {
    "id": "knife",

    "name": "a knife",

    "description":
        "A hunting knife.",

    "mass": 0,

    "interaction": None
}


def inter_decantcure(item_id,object_id):
    from player import inventory
    if (item_id == "boot" or item_id == "goblet") and (item_oldboot in inventory and item_hangover2 in inventory):
        print("You decant the contents of the goblet into the old boot")
        inventory.remove(item_hangover2)
        inventory.remove(item_oldboot)
        inventory.append(item_hangover)
    else:
        print("Nothing interesting happens")


item_oldboot = {
    "id": "boot",

    "name": "a boot",

    "description": "A smelly old boot, gross!",

    "mass": 0,

    "interaction": inter_decantcure
}

item_sword = {
    "id": "sword",

    "name": "a sword",

    "description": "A sharp steel shortsword.",

    "mass": 0,

    "interaction": None
}

item_money = {
    "id": "gold",

    "name": "a pile of gold",

    "description": "Shiny gold!",

    "mass": 0,

    "interaction": None

}


def inter_watergoblet(item_id,object_id):
    from player import inventory
    if item_id == "ingredients" or item_id == "goblet":
        if item_watergoblet in inventory:
            inventory.remove(item_ingredients)
            inventory.remove(item_watergoblet)
            inventory.append(item_hangover2)
            print("You mix the ingredients in the wooden goblet full of water.")
        else:
            print("Nothing interesting happens.")
    else:
        print("Nothing interesting happens")


item_watergoblet = {
    "id": "goblet",

    "name": "a goblet full of water",

    "description": "A typical wooden goblet, filled with water.",

    "mass": 0,

    "interaction": inter_watergoblet
}


def inter_waterboot(item_id,object_id):
    from player import inventory
    if item_id == "ingredients" or item_id == "boot":
        if item_waterboot in inventory:
            inventory.remove(item_ingredients)
            inventory.remove(item_waterboot)
            inventory.append(item_hangover)
            print("You mix the ingredients in the old boot full of water.")
        else:
            print("Nothing interesting happens.")
    else:
        print("Nothing interesting happens")


item_waterboot = {
    "id": "boot",

    "name": "a boot full of water",

    "description": "A smelly old boot, filled with water.",

    "mass": 0,

    "interaction": inter_waterboot

}

item_hangover = {
    "id": "boot",

    "name": "a hangover cure in a boot",

    "description": """A smelly old boot filled with some sort of concoction, 
supposedly it will cure hangovers.""",

    "mass": 0,

    "interaction": None
}

item_hangover2 = {
    "id": "goblet",

    "name": "a hangover cure in a goblet",

    "description": """A simple wooden goblet filled with some sort of concoction,
supposedly it will cure hangovers.""",

    "mass": 0,

    "interaction": inter_decantcure
}

item_ingredients = {
    "id": "ingredients",

    "name": "some ingredients",

    "description": "A powerful mixture of herbs with a strong aroma.",

    "mass": 0,

    "interaction": inter_waterboot

}


def inter_smashgrate(item_id,object_id):
    from player import inventory
    from player import current_room
    from map import rooms
    global current_room
    if item_id == "rock":
        inventory.remove(item_rock)
        print("""You smash the grating with the rock,
a small hole is opened. You can see light outside...""")
        input("Press ENTER to continue...")
        print("""You crawl through the small space and your eyes
struggle to adjust to the bright sunlight.""")
        current_room = rooms["Courtyard"]
        from game import main
        main()


item_rock = {
    "id": "rock",

    "name": "a rock",

    "description": "a large rock",

    "mass": 0,

    "interaction": None

}
time_counter = 0
def inter_turner(item_id,object_id):
    global time_counter
    if time_counter<3:

        if object_id== "wizard":
            print("""You suddenly feel dizzy and your vision starts to spin. Before you blackout you have a vision. 

You realise that you are standing in the Throne Room stood before the empty throne but you notice that the fabric is different, it doesn't look as dusty as it did before. 
There is an orange hue which complements the azure banners that are hanging from the ceiling,
Your vision shifts and begins to bounce as you make your way across the room. You stop to admire the paintings on the wall, but one stands out to you in particular.
As an arm reaches up behind the painting, you recognise  the bright saturn sleeve with the clean gold band around the wrist.
It could only be the hand of the wizard which now seems to be empty.
*Whap*
Your vision clears and you are back in the room.  You hear the wizard mumble something about gravy for the brain before stumbling out of the room,
clearly the door to the south is now open again.
""")
            from map import room_greathall, room_throne, room_ante
            from people import people_king, people_viceroy, people_lady, people_soldier1, people_soldier2
            room_greathall["people"] = {"king":people_king, "viceroy": people_viceroy, "catherine": people_lady, "thomas": people_soldier1, "captain": people_soldier2}
            room_greathall["objects"] = [object_king, object_viceroy, object_lady2, object_soldier1, object_soldier2]
            room_greathall["exits"] = {"west": "Throne Room"}
            room_ante["exits"] = {"south": "Great Hall"}
            room_ante["people"] = {}
            room_ante["objects"] = {}
            room_greathall["description"] = """The door to the anteroom immediately locks behind you.
The room is different to how you saw it before, everything has been cleaned and servants are preparing the table.
Everyone except the wizard is in here sitting down waiting for a meal with their drinks.
The exits to the courtyard and battlements are bolted shut, must be a lock in.
This seems like the perfect opportunity to make your move. The wizard's vision must have been a clue, maybe you should check the throne room."""
            room_throne["description"] = """The room is quiet and still. You instantly recognise the painting on the far wall from your vision of the wizard's past.
You remove it from the wall, look behind it and see a bottle of poison."""
            room_throne["items"] = [item_poison]
            room_throne["people"] = {}
            room_throne["objects"] = ()
        elif object_id== "king":
            print("""You suddenly feel dizzy and your vision starts to rotate. 

When your view becomes clear again, you find that you are standing in the your uncle’s chamber, and your father, the old king, is also in the chamber although he looks much younger than you remember.
Old king:”How dare you to do such a thing, like falling in love with a man! Think of the reputation of our kingdom!”
Uncle:”Is my sexual orientation the original sin or you are just afraid my existence is a threat to your throne?”
The viceroy went to find your uncle after the old king left.
Viceroy:” The only way for you to get past this is to kill the king and then you will be next in line. Then no one will restrict who you fall in love with.”
…
This starts a  war between Otterberg and Aragon, the king went to the field himself. Although Otterberg won the battle, the king got injured.
The assassins were too afraid and reluctant to kill the old king, so the new king knew he had to kill the old king himself.
The old king was found dead during the journey back from the war, it was suspected that he died to poison.
*Whap*
Your vision clears and you are back in the room.
""")
        elif object_id== "viceroy":
            print("""You suddenly feel dizzy and your vision starts  to rotate.

When your vision becomes clear again, you find yourself standing in the mayor’s office. 
The viceroy, the biggest coal merchant in the kingdom, is facing a charge of selling the royal family unqualified goods. 
“Viceroy, I have received a letter from an officer. ”
After reading the letter, viceroy: “This cannot be  true, there is nothing wrong with my goods, they are as legitimate as they could be. ”
“I do not doubt that but...you know, you shouldn’t offend the royal family. ”
The Viceroy tries to appeal to his honesty and legitimacy of his goods  but in the end he not only would have to reduce the price of his goods but would also be amerced for his alleged offenses.
From this point onwards, the viceroy’s lust for power only grew more and more.  
To become more powerful, he needed a puppet king, so his attention was drawn towards the king’s weaker brother.
He decided that he would manipulate the king’s brother to kill the king, for if he had the new king in his pocket, he would be both the richest and the most powerful man in the kingdom.
*Whap*
Your vision clears and you are back in the room.
""")
        elif object_id== "catherine":
            print("""You suddenly have a strange feeling of dizziness  and your vision starts to spin.
            
When your view becomes clear again, you find yourself standing in the middle of a throne room with the emblem of Aragon just beyond the throne.
You realise that  you are at the crowning ceremony of Aragon’s new king, Catherine’s brother. The whole kingdom are celebrating except for the king’s sister;
you can see the rage and annoyance on the lady’s face.
*Whap*
Your vision starts to rotate again, you hear the lady is asking for a marriage alliance and the unwelcome feeling you get makes you feel that something terrible is in the works.
""")
        elif object_id== "captain":
            print("""You suddenly feel dizzy and your vision starts to spin.  

You find yourself in a tavern. You notice that the soldier is sat drinking around a table with what looks like his friends.
Nothing here seems to be of much use to you. Maybe you shouldn’t have used the time turner on the soldier…
*Whap*
Your vision clears and you are back in the room.
""")
        elif object_id== "thomas":
            print("""You suddenly feel dizzy and your vision starts to spin. 
You find yourself stood next to a cot. There is a baby sleeping peacefully in the cot. Could it be the soldier?
*Whap*
Your vision clears and you are back in the room.
""")
        else:
            print("Nothing happens")
            return
        time_counter += 1
    else:
        print("You have used up the magic in this artifact")

item_time_turner = {
    "id": "timeturner",

    "name": "the Timeturner",

    "description": "a magical artifact that looks into people's past",

    "mass": 0,

    "interaction": inter_turner
}

item_poison = {
    "id": "poison",

    "name": "poison",

    "description": "A powerful poison",

    "mass": 0,

    "interaction": None
}
object_grate = {
    "id": "grate",

    "description": "Some wrought iron grating in the wall",

    "interaction": inter_smashgrate

}

object_bed = {
    "id": "bed",

    "description": """Quite a plush bed for a prison, although it would've been better 
if it wasn't right next to a draughty wall grate""",

    "interaction": None
}


def inter_fountain(item_id,object_id):
    from player import inventory
    if item_id == "boot" and item_oldboot in inventory:
        inventory.remove(item_oldboot)
        inventory.append(item_waterboot)
        print("You fill the old boot up with water.")
    elif item_id == "goblet":
        inventory.remove(item_goblet)
        inventory.append(item_watergoblet)
        print("You fill the wooden goblet up with water.")
    else:
        print("Nothing interesting happens")


object_fountain = {
    "id": "fountain",

    "description": "An ornate water feature",

    "interaction": inter_fountain
}

object_flowerpot = {
    "id": "flowerpot",

    "description": "A smart ceramic flowerpot with some bright flowers in",

    "interaction": None
}

object_lady = {
    "id": "catherine",

    "description":
        """Catherine of Aragon,
a noble lady from a different land.
She is weathly and well-spoken, although she
still speaks with a Franco-Spanish accent.""",

    "interaction": None
}

object_lady2 = {
    "id": "catherine",

    "description":
        """Catherine of Aragon,
a noble lady from a different land.
She is weathly and well-spoken, although she
still speaks with a Franco-Spanish accent.""",

    "interaction": inter_turner
}


def inter_cure(item_id, object_id):
    from player import inventory
    if item_id == "boot" and item_hangover in inventory:
        from conversations import conv_wizard
        print("You give the smelly old boot containing a hangover cure to the wizard.")
        print("The wizard sniffs it curiously. Then proceeds to drink the contents...\n")
        inventory.remove(item_hangover)
        print("""The wizard seems to recover from his hangover instantly!
If only you knew what ingredients the lady used to make such a potion.""", "\n")
        print("\"I cannot talk here. Meet me in the anteroom to the north\"\n")
        conv_wizard["opening"] = people_conversations["wizard_cured"]
        conv_wizard["questions"] = people_conversations["Qwizard_cured"]
        conv_wizard["responses"] = people_conversations["Rwizard_cured"]

        from map import room_greathall
        from map import room_ante
        from people import people_wizard

        room_greathall["description"] = """A Grand hall, with fine tapestries and paintings on every wall.
A straight oak table stands in centre of the hall
with many chairs. At the head of the table,
a grand gilded chair dominates the room."""
        room_ante["description"] = """The room is the same as ever. However you now happen to notice an odd picture on the wall with a
mechanical dial next to it."""
        room_greathall["people"] = {}
        room_greathall["objects"] = []
        room_greathall["items"] = []
        room_ante["people"] = {"wizard": people_wizard}
        room_ante["objects"] = [object_wizard, object_dial, object_painting]
        object_wizard["interaction"] = inter_turner







    elif item_id == "goblet" and item_hangover2 in inventory:
        print("*The wizard bats the goblet away*")
        print("\"$!&@*! I will never drink from such a thing of my own will!\"")
        print("(Looks like you'll need to find something else to contain the cure)")

    else:
        print("Nothing interesting happens")

object_wizard = {
    "id": "wizard",

    "description":
        """Clearly only a shadow of his former self,
hungover or still possibly drunk from the night before,
he sits mouth open with his head back, snoring loudly.""",

    "interaction": inter_cure

}

object_king = {
    "id": "king",

    "description":
        """This is King Wattus Rex.""",

    "interaction": inter_turner

}

object_viceroy = {
    "id": "viceroy",

    "description":
        """This is the viceroy. Not well liked around here.""",

    "interaction": inter_turner

}


def inter_gold(item_id,object_id):
    from player import inventory
    if item_id == 'gold' and item_money in inventory:
        print("\"Ah gold, that's loosened my lips a little.")
        print("Gaius is the old drunken wizard in the great hall.\"")
        inventory.remove(item_money)
        from conversations import conv_soldier1
        from conversations import conv_lady
        conv_soldier1["questions"] = people_conversations["Qsoldier_paid"]
        conv_soldier1["responses"] = people_conversations["Rsoldier_paid"]
        conv_lady["questions"] = people_conversations["Qlady_change1"]
        conv_lady["responses"] = people_conversations["Rlady_change1"]
        from map import room_courtyard
        room_courtyard["puzzles"] = people_conversations["Plady_riddle"]
        object_soldier1["interaction"] = inter_turner
    else:
        print("Nothing interesting happens")


object_soldier1 = {
    "id": "thomas",

    "description":
        """A strong soldier.""",

    "interaction": inter_gold

}

object_soldier2 = {
    "id": "captain",

    "description":
        """This is the captain of the guard. A master of military tactics""",

    "interaction": inter_turner
}

object_guard = {
    "id": "guard",

    "description":
        """The guard is sound asleep, how cliché""",

    "interaction": None
}

object_painting = {
    "id": "painting",

    "description": """
           
                           A
                     ooo OOO OOO ooo
             J  oOO       /  \       OOo   C
             oOO         /    \         OOo
          oOO           /      \           OOo
     F  oOO            /        \             OOo   X
      oOO    _________/________  \__________   OOo
     oOO     \       /            \        /     OOo
    oOO       \     /              \      /       OOo
   oOO         \   /                \    /        OOo
   oOO          \ /                  \  /         OOo  L
   oOO           /                    \/          OOo
 Q oOO          / \                  / \          OOo
   oOO         /   \                /   \         OOo
    oOO       /     \              /     \       OOo
     oOO     /_______\____________/_______\     OOo
      oOO             \          /             OOo
        oOO            \        /             OOo   G
       Y  oO            \      /            OOo
             oOO         \    /          OOo
                 oOO      \  /        OOo   N
             K        ooo OOO OOO ooo
                            B


'WHEN THE POINTS OF THE SOLOMONS SEAL BEFALLS ON THIS KINGDOM
        THE DORMANT CLOCK WILL START TO RUN'
                           """,

    "interaction": None
}

object_dial =  {

    "id": "dial",

    "description":
        """A mechanical circular dial with the letters of the alphabet on,
used for entering codes.""",

    "interaction": None
}
