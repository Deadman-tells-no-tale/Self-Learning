# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
heights = 0
for x in range (0, (n+1)):
    heights += int(student_heights[x])
average = round(heights / (n+1))
print(average)