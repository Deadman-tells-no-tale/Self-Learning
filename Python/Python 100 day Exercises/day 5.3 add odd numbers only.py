#Write your code below this row 👇
decadelist=[]

for counter in range(0,101):
    decadelist.append(counter)

totalnumber=0
for count in range(0,(counter + 1)):
    if decadelist[count] %2 != 0:
        totalnumber += decadelist[count]
        print(totalnumber)
print(totalnumber)