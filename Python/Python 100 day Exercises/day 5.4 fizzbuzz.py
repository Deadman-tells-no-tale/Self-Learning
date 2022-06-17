#for anything divisbile by 3 = fizz
#for anything divisible by 5 = buzz
#for anything divisibile by both = fizz buzz

for number in range(1,101):
    if number % 3 ==0 and number %5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print ("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
