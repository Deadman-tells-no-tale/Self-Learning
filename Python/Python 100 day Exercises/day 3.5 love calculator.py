# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#check for TRUE LOVE
from collections import Counter

lowered_name1 = name1.lower() 
lowered_name2 = name2.lower()
lovers = str(name1.lower() + name2.lower())

truecount1 = Counter(lovers)
true_score = str(truecount1["t"] + truecount1["r"] +truecount1["u"]+truecount1["e"])
love_score =str(truecount1["l"]+truecount1["o"]+truecount1["v"]+truecount1["e"])
namecount = true_score + love_score 
love_count = int(namecount)

if love_count <= 10 or love_count >= 90:
    print(f"Your score is {love_count}, you go together like coke and mentos.")
elif love_count >= 40 and love_count <= 50:
    print(f"Your score is {love_count}, you are alright together.")
else:
    print(f"Your score is {love_count}.")