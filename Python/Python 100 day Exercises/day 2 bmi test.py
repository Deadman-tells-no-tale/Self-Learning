# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

heightsquared = float(height) * float(height)
bmi = float(int(weight) / (float(height) * float(height)))
roundedbmi = int(round(bmi))
print(roundedbmi)