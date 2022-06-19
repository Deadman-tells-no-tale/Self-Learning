#how many letter does user want
#how many symbols does user want
#how many numbers does user want

import random
import string
import time
import os

abc=string.ascii_lowercase
cap_abc=string.ascii_uppercase
number = [0,1,2,3,4,5,6,7,8,9]
spec_char=[".","!","@","#","$","%","&","+","?","*","="]
pass_options = []


passlength = int(input("How long of a password would you prefer?(the bigger the better): "))
if passlength == 0:
    print("Then why did you start this? Please come back when you need a password.")

else:    
    alphabit_amount = int(input("How many letters would you like in your password?: "))
    if alphabit_amount > int(passlength):
        print("Error: The amount you have chosen is to large. I\"ll add a random one for you")
        alphabit_amount = random.randint(0,(passlength))
        print(f"I've selected {alphabit_amount} instead.")
    elif alphabit_amount == 0:
        pass
    else:
        pass_options.extend(abc)
        pass_options.extend(cap_abc)
    print(f"You now have this much space left in your password amount({passlength}):"+ str(passlength - alphabit_amount))
    


    num_amount = int(input("How many numbers would you like in your password?: "))
    if num_amount > (passlength-alphabit_amount):
        
        print("Error: The amount you have chosen is to large. I\"ll add a random one for you")
        num_amount = random.randint(0,(passlength - alphabit_amount))
        print(f"I've selected {num_amount} instead.")
    elif num_amount == 0:
        pass
    else: 
        pass_options.extend(number)
    print(f"You now have this much space left in your password amount({passlength}):"+ str(passlength - alphabit_amount-num_amount))

    spec_amount= int(input("How many special characters would you like?: "))
    if spec_amount > (passlength-alphabit_amount-num_amount):
        print("Error: The amount you have chosen is to large. I\"ll add a random one for you")
        spec_amount = random.randint(0,(passlength-alphabit_amount-num_amount))
        print(f"I've selected {spec_amount} instead.")
    if spec_amount == 0:
        pass
    else:
        pass_options.extend(spec_char)
        




    print(f"You're Pass length you've chosen is: {passlength}, The amount of letters chosen is: {alphabit_amount}, The number amount chosen is: {num_amount} and the special characters chosen is: {spec_amount}.")
    print("Generating ... Please wait")
    time.sleep(3)

    randchar =[]
    random_special = []
    random_number = []
    random_pass = []
    newpassword=""

    for abc_counter in range(0, passlength):
        if pass_options == []:
            print("I can't run with nothing... You know what i'll make one up for you. Please wait...")
            time.sleep(2)
            for newabc_counter in range(0,passlength):
            
                randchar += pass_options[random.randint(0,3)]
                length = int(len(randchar))-1
                randpos = random.randint(0,length)
                random_pass += str(randchar[randpos])
                randchar=[]
                abc_counter += 1
            newpassword = randchar
            print(f"Here you go:{newpassword}!")
        
    else:        
        pass_choices= len(pass_options)
        randchar += pass_options[random.randint(0,pass_choices)]
        length = int(len(randchar))-1
        randpos = random.randint(0,length)
        random_pass += str(randchar[randpos])
        print(random_pass)
        abc_counter += 1
    Password = (random_pass)
    print(f"Here is the suggested Password: \"{Password}\"")