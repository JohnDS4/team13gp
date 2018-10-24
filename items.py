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
item_time_turner = {
    "id": "timeturner",

    "name": "a time-turner",

    "description": "a magical artifact that looks into people's past",

    "mass": 0,

    "interaction": None
}
time_counter = 0
def inter_turner(item_id,object_id):
    global time_counter
    if time_counter<3:

        if object_id== "wizard":
            print("wizard's past ###")
        elif object_id== "king":
            print("wizard's past ###")
        elif object_id== "viceroy":
            print("wizard's past ###")
        elif object_id== "catherine":
            print("wizard's past ###")
        elif object_id== "thomas":
            print("wizard's past ###")
        elif object_id== "captain":
            print("wizard's past ###")
        else:
            print("Nothing happens")
            return
        time_counter += 1
    else:
        print("You have used up the magic in this artifact")


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


def inter_cure(item_id, object_id):
    from player import inventory
    if item_id == "boot" and item_hangover in inventory:
        from conversations import conv_wizard
        print("You give the smelly old boot containing a hangover cure to the wizard.")
        print("The wizard sniffs it curiously. Then proceeds to drink the contents...\n")
        inventory.remove(item_hangover)
        print("""The wizard seems to recover from his hangover instantly!
        If only you knew what ingredients the lady used to make such a potion.""", "\n")
        print("I cannot talk here. Meet me in the anteroom")
        conv_wizard["opening"] = people_conversations["wizard_cured"]
        conv_wizard["questions"] = people_conversations["Qwizard_cured"]
        conv_wizard["responses"] = people_conversations["Rwizard_cured"]

        from map import room_greathall
        from map import room_ante
        from people import people_wizard

        room_ante["description"] = "new desc. ###"
        room_greathall["people"] = {}
        room_ante["people"] = {"wizard": people_wizard}

        object_wizard["interaction"] = inter_turner






    elif item_id == "goblet" and item_hangover2 in inventory:
        print("*The wizard bats the goblet away*")
        print("$!&@*! I will never drink from such a thing of my own will!")
        print("(Looks like you'll need to find something else to contain the cure)")

    else:
        print("Nothing interesting happens")

object_wizard = {
    "id": "wizard",

    "description":
        """Clearly only a shadow of his former self,
    hungover or still possibly drunk from the night before,
    he sits mouth open with his head back, snoring loudly.""",

    "interaction": inter_turner

}

object_king = {
    "id": "king",

    "description":
        """This is the king.""",

    "interaction": None

}

object_viceroy = {
    "id": "viceroy",

    "description":
        """This is the viceroy.""",

    "interaction": None

}


def inter_gold(item_id,object_id):
    from player import inventory
    if item_id == 'gold' and item_money in inventory:
        print("Ah gold, that's loosened my lips a little.")
        print("Gaius is the old drunken wizard in the great hall.")
        inventory.remove(item_money)
        from conversations import conv_soldier1
        from conversations import conv_lady
        conv_soldier1["questions"] = people_conversations["Qsoldier_paid"]
        conv_soldier1["responses"] = people_conversations["Rsoldier_paid"]
        conv_lady["questions"] = people_conversations["Qlady_change1"]
        conv_lady["responses"] = people_conversations["Rlady_change1"]
        from map import room_courtyard
        room_courtyard["puzzles"] = people_conversations["Plady_riddle"]
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
        """This is the captain of the guard.""",

    "interaction": None
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
