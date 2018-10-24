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
    "wizard_cured" : """"I'm sorry that I could not speak to you back in there. The viceroy has eyes everywhere, but we should be ok in this room.
I am Gaius and I know why you are here.
I can help you get your revenge on the person that killed your parents, but I don't have much time. 
The king keeps me drunk with the enchanted golden goblet that he keeps next to his throne.
Please 'examine' this painting on the wall, in it is a secret code. 'Adjust' the dial next to it to the correct code and you will have access to the
contents behind it - The Timeturner.
You can use that to see into the past of up to 3 people. However, once you gain access to it, this room will be locked and you cannot leave to
stop it getting into the wrong hands. The item must be used on me first while in here for you to gain access back to the rest of the castle.
Good luck!"

You can see the wizard's eyes start to look more glazed. He is clearly becoming drunk again.
""",
    "Qwizard_cured" : ["I'm still confused, help me!"],
    "Rwizard_cured" : [""""WHA? You don't know who you're talking to young man! I was here when this castle was built and I certainly won't be leaving anytime soon..."

The wizard is clearly hammered. Great.
"""],
    "Qsoldier_paid" : ["Can you tell me who Gaius is now?", "Can I play a game?"],
    "Rsoldier_paid" : ["\"I told you, he is the drunken old wizard staying in the great hall\"", "\"Sure, you can 'PLAY DICE' with me\""],
    "Qlady_change1" : ["I know Gaius is the drunken old wizard, can you help me cure him?"],
    "Rlady_change1" : ["""\"Ok, but first I must test you. Answer me this riddle:

'What's black when you buy it, red when you use it and white when you throw it away?'
When you are ready, 'ANSWER' the 'RIDDLE'.\""""],
    "Plady_riddle" : [riddle_lady]
}
