# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 * 4) / 5

#                            = 1.6

# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input
# test_h = 3
# test_w = 9
# Example Output
# You'll need 6 cans of paint.
# Hint
# 1. To round up a number:

# https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python use math.ceil

# 2. Make sure you name your function/parameters the same as when it's called on the last line of code.

# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.
#Write your code below this line 👇3
import math
def paint_calc(height,width,cover):
    cans=(height * width)/cover
    rounded=math.ceil(cans)
    print(f"You'll need {rounded} cans of paint.")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
