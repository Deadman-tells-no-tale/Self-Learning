import sys
import random
import time

class player:
    player_alive = True
    player_health = 100
    player_manapool=10
    class race_options:
        def Elf():
            health = 110
        def Golem():
            health = 150
        def Human():
            health = 100


def intro():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print("Welcome to the Treasure Island Text Adventure.")
    print("Dear Adventurer, \nYour mission is to find the treasure on this mysterious island, or atleast die trying.")
    print("When making choices please try to add responses exactly as they are shown and in lower cases please!")
    print("Thank you for playing now enjoy the story!")


#Write your code below this line 👇

player_health = 100
Player_alive = True
Player_inventory={}

def player_death():
    while Player_alive != True:
        if player_health == 0 or player_health < 0:
            print("Oh dear it seems you have passed away...")
            time.sleep(3)
            continue_game = print("try again?: Y or N")
            if continue_game == "Y" or "y":
                print("game continues:")
        else:
            print('''
                                Rest in peace
                                 _____  _____
                                <     `/     |
                                 >          (
                                |   _     _  |
                                |  |_) | |_) |
                                |  | \ | |   |
                                |            |
                 ______.______%_|            |__________  _____
               _/                                       \|     |
              |                                               <
              |_____.-._________              ____/|___________|
                                |            |
                                |            |
                                |            |
                                |            |
                                |   _        <
                                |__/         |
                                 / `--.      |
                               %|            |%
                           |/.%%|          -< @%%%
                           `\%`@|     v      |@@%@%%    - mfj
                         .%%%@@@|%    |    % @@@%%@%%%%
                    _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%
        ''')
            break


print("You wake up on an island with only one desire. You don't remember how you arrived but all you know is that you came for treasure")
location = input("Where would you like to explore? \"Shoreline\", \"Forest\", or the \"Ocean\"")
print(location)
location_choice=location.lower()

if location_choice == "shoreline":
    print("You decided to walk the Shoreline in hopes of finding something interesting...")
    time.sleep(3)
    print("The only intersting thing around was that the island seems very small but the walk made you thirsty. sadly you took 1 damage")
    player_health -= 1
    print(player_health)

elif location_choice == "forest":
        print ("You walked into the forest in search of something intesting...")
        time.sleep(3)
        print("after some time searching around the forest ")
        
else:
    print("oh dear you died")
    player_health -= 100
    print(player_health)
