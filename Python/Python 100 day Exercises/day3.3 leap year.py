# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap = year % 4
if leap == 0:
    if (leap % 100) == 0:
        if (leap % 400) == 0:
            print("Leap year.")
else:
    print ("Not leap year.")
