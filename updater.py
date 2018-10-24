from puzzles import *
room_descriptions = {
	"goblet_removed" : """A Grand hall, with fine tapestries and paintings on every wall.
A straight oak table stands in centre of the hall
with many chairs. At the head of the table,
a grand gilded chair dominates the room.
Slumped head back in another sleeps a raggedy old man.
next to a fireplace, where a handful of coals lie""",

	"boot_removed" : """The wind swept and exposed battlements.
beyond the grey horizon the enemy may lie in waiting.
The few soldiers on duty seem more interested in who'll throw the next combo in their dice game.""",



}

item_room_descriptions = {
	"goblet" : room_descriptions["goblet_removed"],
	"boot" : room_descriptions["boot_removed"]
}

people_conversations = {
	"wizard_cured" : "",
	"Qwizard_cured" : [],
	"Rwizard_cured" : [],
	"Qsoldier_paid" : ["Can you tell me who Gaius is now?", "Can I play a game?"],
	"Rsoldier_paid" : ["I told you, he is the drunken old wizard staying in the great hall", "Sure, you can 'PLAY DICE' with me"],
	"Qlady_change1" : ["I know Gaius is the drunken old wizard, can you help me cure him?"],
	"Rlady_change1" : ["""Ok, but first I must test you. Answer me this riddle:

'What's black when you buy it, red when you use it and white when you throw it away?'
When you are ready, 'answer' the riddle."""],
	"Plady_riddle" : [riddle_lady]
}