# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
heightsquared = float(height) * float(height)
bmi = float(int(weight) / (float(height) * float(height)))
roundedbmi = int(round(bmi))


if roundedbmi < 18.5:
    print(f"Your BMI is {roundedbmi}, you are underweight.")
elif roundedbmi <= 25: 
    print(f"Your BMI is {roundedbmi}, you have a normal weight.")
elif roundedbmi <= 30:
    print(f"Your BMI is {roundedbmi}, you are slightly overweight.")
elif roundedbmi <= 35: 
    print(f"Your BMI is {roundedbmi}, you are obese.")
else: 

    print(f"Your BMI is {roundedbmi}, you are clinically obese.")