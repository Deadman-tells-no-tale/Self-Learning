#how many letter does user want
#how many symbols does user want
#how many numbers does user want

import random
import string



abc=string.ascii_lowercase
ABC=string.ascii_uppercase
number = [0,1,2,3,4,5,6,7,8,9]
spec_char=[".","!","@","#","$","%","&","+","?","*","="]


passlength = input("How long of a password would you prefer?(the bigger the better): ")
alphabit_amount = int(input("How many letters would you like in your password?: "))
if alphabit_amount > int(passlength):
    print("Error: The amount you have chosen is to large. I\"ll add a random one for you")
    alphabit_amount = random.randint(0,passlength)
    print(f"I've selected {alphabit_amount} instead.")
print(f"You now have this much space left in your password amount({passlength}):"+ (passlength - alphabit_amount))


num_amount = input("How many numbers would you like in your password?: ")
if num_amount > (int(passlength)-int(alphabit_amount)):
    print("Error: The amount you have chosen is to large. I\"ll add a random one for you")
    num_amount = random.randint(0,(passlength-alphabit_amount))
    print(f"I've selected {num_amount} instead.")
print(f"You now have this much space left in your password amount({passlength}):"+ (passlength - alphabit_amount-num_amount))
spec_amount= input("How many special characters would you like?: ")

 
if +spec_amount > (int(passlength)-int(alphabit_amount)-int(num_amount)):
    print("Error: The amount you have chosen is to large. I\"ll add a random one for you")
    spec_amount = random.randint(0,(passlength-alphabit_amount-num_amount))
    print(f"I've selected {spec_amount} instead.")


#for abcd in range(0, alphabit_amount):

