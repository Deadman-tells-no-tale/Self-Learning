import random

win_condition = ["win","lose","draw"]
hand = ["rock","paper","scissors"]

player_hand = input("What is your hand choice? rock\"1\" paper\"2\" scissors\"3\"")
user_choice = int(player_hand) - 1
player_hand = hand[user_choice]
print(f"Player chose: {player_hand}")
randomnumber= random.randint(0,2)
computer_hand = hand[randomnumber]
print(f"Computer chooses: {computer_hand}")

if  player_hand == computer_hand:
  print(f"{player_hand} and {computer_hand} are the same it's a {win_condition[2]}!")

elif user_choice == 0 and randomnumber == 2:
  print(f"You Win! \n{player_hand} beats {computer_hand} ")

elif user_choice == 1 and randomnumber == 0:
  print(f"You Win! \n{player_hand} beats {computer_hand} ")
  
elif user_choice == 2 and randomnumber == 1:
  print(f"You Win! \n{player_hand} beats {computer_hand} ")

else:
  print(f"You lose {computer_hand} beats {player_hand} ...")