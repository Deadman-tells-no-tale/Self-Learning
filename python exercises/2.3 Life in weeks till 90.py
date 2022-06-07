# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Day_90 = 90 * 365
weeks_90 =90 * 52
months_90 = 90 * 12


userage = age
userage_remaind = int(Day_90) - (int(age) * 365)
userage_remainw = int(weeks_90) - (int(age) * 52)
userage_remainm = int(months_90) - (int(age) * 12)

print(f"You have {userage_remaind} days, {userage_remainw} weeks, and {userage_remainm} months left.")