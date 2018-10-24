from items import *
from people import *
from puzzles import *

room_courtyard = {
    "name": "Courtyard",

    "description":
    """A square courtyard swept clean
and filled with the sweet smell of jasmine.
In the centre lies a large water fountain.
No furniture to speak of just an ornate door to the grand hall
and an opening that takes you up a wide set of spiral stairs to the battlements.
There are flower pots on the wall with beautiful foxgloves growing in them.
    """,
    # exits/people/items in room will be added using functions in game.py
    # (printed in full sentences)

    "exits": {"north": "Great Hall", "south": "Battlements"},

    "items": [],

    "people": {"lady":people_lady, "catherine":people_lady},

    "puzzles" : [],

    "objects": [object_fountain, object_lady, object_flowerpot]

}

room_greathall = {
    "name": "Great Hall",

    "description":
   	 """A Grand hall, with fine tapestries and paintings on every wall.
On a shelf near the door lies a single wooden goblet.
A straight oak table stands in centre of the hall
with many chairs. At the head of the table,
a grand gilded chair dominates the room.
Slumped head back in another sleeps a raggedy old man.
next to a fireplace, where a handful of coals lie""",

    "exits": {"west": "Throne Room", "south": "Courtyard", "east": "Battlements", "north": "Anteroom"},

    "items": [item_goblet],

    "people": {"wizard":people_wizard},

    "puzzles" : [],
	
    "objects": [object_wizard]

}

room_throne = {
    "name": "Throne Room",

    "description":
    """This is the throne room. TODO ---""",

    "exits": {"east": "Great Hall"},

    "items": [],

    "people": {"king":people_king,
               "viceroy":people_viceroy},

    "puzzles" : [],
	
    "objects": [object_king, object_viceroy]

}

room_battlements = {
    "name": "Battlements",

    "description":
    """The wind swept and exposed battlements.
beyond the grey horizon the enemy may lie in waiting.
The few soldiers on duty seem more interested in who'll throw the next combo in their dice game.
There is a single old boot in the middle of the walkway which seems odd to you.""",

    "exits": {"west": "Great Hall", "north": "Courtyard"},

    "items": [item_oldboot],

    "people": {"soldier":people_soldier1, "thomas":people_soldier1, "captain":people_soldier2},

    "puzzles" : [dice_game],

    "objects": [object_soldier1, object_soldier2]

}

room_ante = {
    "name": "Anteroom",

    "description": """This is a mostly unused room in the castle. A few pieces of furniture here and there but other than that it is fairly nondescript.""",

    "exits": {"south": "Great Hall"},

    "items": [item_time_turner],

    "people": {},

    "puzzles" : [dial_game],

    "objects": [object_painting, object_dial]

}

room_jail = {
    "name": "Jail",

    "description":
    """You are in a dank prison cell. The gate is locked tight and a guard is on duty outside.
There is a bed in the corner. The room is in a poor state, which is no surprise. Bits of rock
from the wall are falling away onto the floor.""",

    "exits": {},

    "items": [item_rock],

    "people": {},

    "puzzles" : [],
	
    "objects": [object_grate, object_bed, object_guard]

}


rooms = {
    "Courtyard": room_courtyard,
    "Great Hall": room_greathall,
    "Throne Room": room_throne,
    "Battlements": room_battlements,
    "Anteroom": room_ante,
    "Jail": room_jail
}