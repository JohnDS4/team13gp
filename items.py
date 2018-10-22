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
    "A standard wooden goblet. It has split and is pretty much unusable.",

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

item_oldboot = {
    "id": "boot",

    "name": "a boot",

    "description": "A smelly old boot, gross!",

    "mass": 0,
	
	"interaction": None
}

item_sword = {
    "id": "sword",
    
    "name": "a sword",

    "description": "A sharp steel shortsword.",

    "mass": 0,
	
	"interaction": None
}

item_potionbook = {
    "id": "book",
    
    "name": "a book",

    "description": "A book of potions *TODO-- ",

    "mass": 0,
	
	"interaction": None
}

def inter_waterboot(item_id):
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
	"id": "hangover",
	
	"name": "a hangover cure",
	
	"description": """A smelly old boot filled with some sort of concoction, 
supposedly it will cure hangovers.""",
	
	"mass": 0,
	
	"interaction": None
}


item_ingredients = {
	"id": "ingredients",
	
	"name": "some ingredients",
	
	"description": "A powerful mixture of herbs with a strong aroma.",
	
	"mass": 0,
	
	"interaction": inter_waterboot
	
}

def inter_fountain(item_id):
	from player import inventory
	if item_id == "boot" and item_oldboot in inventory:
		inventory.remove(item_oldboot)
		inventory.append(item_waterboot)
		print("You fill the old boot up with water.")
	else:
		print("Nothing interesting happens")

object_fountain = {
	"id": "fountain",
	
	"description": "An ornate water feature",
	
	"interaction": inter_fountain
}

object_lady = {
	"id": "lady",
	
	"description":
    """This is the lady.""",
	
	"interaction": None
	
}

object_wizard = {
	"id": "wizard",
	
	"description":
    """This is the wizard.""",
	
	"interaction": None
	
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

object_soldier1 = {
	"id": "soldier",
	
	"description":
    """This is the soldier.""",
	
	"interaction": None
	
}

object_soldier2 = {
	"id": "warrior",
	
	"description":
    """This is the warrior.""",
	
	"interaction": None
	
}

