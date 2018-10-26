﻿#game to simulate a text based fight between a computer and a player
#imported modules time, string, random, and os 
# os to wipe screen !!!only works on windows!!! 
import time
import string 
import random 
import os

player = {
        "id":"player",
        "name":"You",
        "health": 100.00

} 

computer = {
        "id":"Viceroy",
        "name":"Viceroy",
        "health":100.00
}
accsi_print = {
        1:"""
+-+
|1|
+-+""",
        2:"""+-+
|2|
+-+""" , 
        3:"""
+-+
|3|
+-+""",
        4:"""
+-+
|4|
+-+""",
        5:"""+-+
|5|
+-+""", 

}
art = {
        1:"""            _ _  __                           _          _   _            
           | (_)/ _|                         | |        | | | |           
           | |_| |_ ___  __      ____ _ ___  | |__   ___| |_| |_ ___ _ __ 
           | | |  _/ _ \ \ \ /\ / / _` / __| | '_ \ / _ \ __| __/ _ \ '__|
           | | | ||  __/  \ V  V / (_| \__ \ | |_) |  __/ |_| ||  __/ |   
           |_|_|_| \___|   \_/\_/ \__,_|___/ |_.__/ \___|\__|\__\___|_|   
                                                                          
                                                                          
                 _   _                       _            _   _     
                | | | |                     | |          | | | |    
                | |_| |__   __ _ _ __     __| | ___  __ _| |_| |__  
                | __| '_ \ / _` | '_ \   / _` |/ _ \/ _` | __| '_ \ 
                | |_| | | | (_| | | | | | (_| |  __/ (_| | |_| | | |
                 \__|_| |_|\__,_|_| |_|  \__,_|\___|\__,_|\__|_| |_|""",
        2:"""
              .%%..%%...%%%%...%%..%%...........%%%%...%%%%%...%%%%%%.
              ..%%%%...%%..%%..%%..%%..........%%..%%..%%..%%..%%.....
              ...%%....%%..%%..%%..%%..........%%%%%%..%%%%%...%%%%...
              ...%%....%%..%%..%%..%%..........%%..%%..%%..%%..%%.....
              ...%%.....%%%%....%%%%...........%%..%%..%%..%%..%%%%%%.
              ........................................................
  .%%..%%..%%%%%%...%%%%...%%%%%%...%%%%...%%%%%...%%%%%%...%%%%...%%..%%...%%%%..
  .%%..%%....%%....%%..%%....%%....%%..%%..%%..%%....%%....%%..%%..%%..%%..%%.....
  .%%..%%....%%....%%........%%....%%..%%..%%%%%.....%%....%%..%%..%%..%%...%%%%..
  ..%%%%.....%%....%%..%%....%%....%%..%%..%%..%%....%%....%%..%%..%%..%%......%%.
  ...%%....%%%%%%...%%%%.....%%.....%%%%...%%..%%..%%%%%%...%%%%....%%%%....%%%%..
  ................................................................................"""
}


def fight(player = player,computer = computer):
        '''this function takes a player dict and people dict as input
        fight(people_player{} , people_x{})'''
        t = time.sleep(1)
        while True:
                t = 0.5
                #while function for fight 
                if player["health"] <= 0:                       
                        print(art[1])
                        time.sleep(2)
                        break
                elif computer["health"] <= 0:
                        print(art[2])
                        import winsound
                        winsound.PlaySound("victory.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                        time.sleep(2)
                        break
                #breaks fight s
                a = random.randint(1,5)         
                print(accsi_print[a])
                time.sleep(t)
                os.system('cls')
                #choses and prints player number to input 
                try:
                        b = int(input("Enter number: "))
                except ValueError:
                        print("That's not a number!")
                        player["health"] -= 15
                        print("you'll be defeted soon")
                        time.sleep(1)
                        continue
                
                        
                
                '''logic to deturmand fight'''
                if b != a:
                        player["health"] -= 15
                        print("you'll be defeted soon")
                        time.sleep(1)
                        os.system('cls')
                elif b == a and computer["health"] > 50:
                        computer["health"] -= 15
                        print("you're growing weaker with every strike %s \n computer health is %s" % (computer["name"], computer["health"]))
                        time.sleep(2)
                        os.system('cls')
                elif b != a and player["health"] > 50:
                        computer["health"] -= 15
                        print("you're growing weaker with every strike %s \n computer health is %s" % (computer["name"], computer["health"]))
                        time.sleep(2)
                        os.system('cls')        
                elif b == a and  computer["health"] < 50:
                        computer["health"] -= 15
                        print("Your reign of terror is almost over %s \n computer health is %s" % (computer["name"], computer["health"]))
                        time.sleep(2)
                        os.system('cls')
                        t = 0.5
                elif b != a and player["health"] < 50 :
                        computer["health"] -= 15
                        print("You've been pretending all time %s \n but you cant pretend in combat" % (player["name"]))
                        time.sleep(2)
                        os.system('cls')
                        t = 1

fight(player,computer)


