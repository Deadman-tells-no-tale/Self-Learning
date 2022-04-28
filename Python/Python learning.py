#LISTS 
##Friends = ["kevin,"Karen","jim"] creating a variable w an array
#friends[1] = "mike"

#LIST FUNCTIONS
#from curses import meta
#from sys import meta_path
#from tty import setcbreak
#from turtle import up
#imprts? above

lucky_numbers = [4,8,15,16,23,42]
friends = ["kevin","Karen","Jim","Oscar","Toby"]
friends.insert (1, "Kelly")
friends.insert ("Larry")
friends.remove ("jim")
friends.append ("james")
#append adds the item at the end while insert is at the beginning if no placement is made
#friends.clear() Empties the list
#friends.pop() removed the last value in the array

print (friends)
print(friends.index("Kelly"))
#print(friends.count("Jim")) allows to see how many of this name exist in the array
#friends.sort (places them in ascending order)
#reversing a list: lucky_numbers.reverse()
friends2 = friends.copy
print(friends2)

#TUPLES
#type of data structure that stores DIFFERENT Values the difference inutable (can't be changed or modified)
coordinates = (4,5)
#if you try to change like coordinates [1] = 10 it will error out if you try to change it.
print(coordinates[0]) 
print (coordinates[1])
#the [] is for the index of the tuple
#lists use [] tuples use ()
#you can make a list of tuples
coordinates2 = [(4,5), (6,7), (80, 34)]
print(coordinates2)


#FUNCTIONS
#collection of code
def name_function():
#def = a keyword 
#def {name of the function} (code entered is indented below but fills parenthesis of function) ends w a colon:
    Variable = "test"
    print(Variable)
#you now need to call the function for it to be ran properly
name_function()
#the above is how you call a function calling will be able to call something above or elsewhere
#functions are best concatenated in "lower_cased" 
#parameters are able to be given to a function
def say_hi(name):
    print("Hello " + name)
say_hi("Mike")
say_hi("when called each time we have to add a name and this is the name")
#if you add age you then type def say_hi(name,age):
#       Print("hello " + name + ", you are " + str(age))

#you can add all types of parameters such as boolians variables and so forth



#RETURN STATEMENT
#returns allows us to get information back or value to view if the function worked,gives us info or not
def cubing_a_number(number):
    number*number*number
    
#cubing_a_number(#)  this doesn't do anything
print(cubing_a_number(3))
#correct way
def cubing_a_number_correctly(number):
    return number*number*number
    print("code")
#cubing_a_number(#)  this will return the value but return stops the function so anything after will never run.
print(cubing_a_number_correctly(3))

result = cubing_a_number_correctly(4)
print(result)


#IF ELSE STATES+MENTS
#if else elseif (elif)/ operators = or, and, >, <, <=, =>, ==, not (makes some true if false)
is_male = True
is_tall = True
#if is_male or is_tall:
if is_male and is_tall:
    print("Tall Male is true")
elif is_male and not(is_tall):
    print ("Short Male is true")
elif not(is_male) and is_tall:
    print("Male is false but is a tall person is true")
else:
    print("neither tall or male")



#I wake up
#if i'm hungry
#    I eat breakfat

#I leave my house:
#if it's cloudy
#    I bring an umbrella
#otherwise
#    I bring sunglasses
#
#I'm at a restruant
#if i want meat
#    I order a setcbreak
#orthwise if I want pasta
#    I order spaghetti & meatballs
#otherwise
#    I order a salad
