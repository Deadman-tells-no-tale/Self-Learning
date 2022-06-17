# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

score = 0
for loop_count in range (0, (n+1)):
    if score < student_scores[loop_count]:
     score = int(student_scores[loop_count])

print(f"The highest score in the class is: {score}")

