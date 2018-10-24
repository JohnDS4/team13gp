from puzzles import *
conv_king = {
    "opening": "(The king ignores you)\n",

    "questions": ["Hello?"],

    "responses": ["The viceroy interjects: \"Don't speak unless spoken to!\""] #Name of king of southern saxons (Sussex 692 - c. 700)

}

conv_viceroy = {
    "opening": """\"If your per capita bean counting troubles you, clerk,
a 'decapita' can be arranged!\"\n""",

    "questions": ["How are you?", "What is your name?"],

    "responses": ["\"I was better before you arrived in this kingdom.\"", "(The viceroy ignores you)"]

}

conv_wizard = {
    "opening": "\"Touch my glass and I'll...@#*% kill you!\"\n",

    "questions": ["What is your name?", "Are you ok?"],

    "responses": ["\"@!*&$, GET OUT OF HERE!\"", 
    "\"NO! I have a splitting headache and don't need to be pestered by you!\"\n(The old man seems to have a hangover)"]

}

conv_lady = {
    "opening": """"Bon dia, clerk, you rise early."\n""",

    "questions": ["Have we met before?", "Can you help me find Gaius?"],

    "responses": ["""\"I believe you'd recall if we had.
I am called Catherine, I am from Aragon.
My father sent me to this island, for what? 
I not sure, the king has no interest in women,
and his viceroy is nothing more than a merchant of lies.\"""",
"""\"I don't think I'm the person to ask that.\""""]

}

conv_soldier1 = {
    "opening": "(The soldier is fully focused on his game)\n",

    "questions": ["How are you?", "Can I play a game?", "Can you tell me who Gaius is?"],

    "responses": ["\"The dice are not going my way today.\"", "\"Sure, I'll 'PLAY DICE' with you\"", "\"I don't talk for free\""]

}

conv_soldier2 = {
    "opening": "...\n",

    "questions": ["How are you?", "What is your name?"],

    "responses": ["\"I'm good.\"", "\"You don't need to know my name.\""]

}
