#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'smallestString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def smallestString(s):
    s="abaacbac"
    # Write your code here
    #string into list or an array
    #if else statement <
   # a=1
   # b=2
   # c=3
    #abc individually checked per section need a loop.
    
    newstring = ''
    numA = s.count('a')
    numB = s.count('b')
    numC = s.count('c')
    #"abaacbac"
    #"abacabac"
    #s[0]
    
    letter = 0
    i = 0
    while letter < len(s) and s[letter] != 'c' :
        if s[letter] == ('a'):
            newstring += "a"
            numA -= 1
        letter += 1
        i += 1

    #"aaa"    
    while numB > 0:
            newstring += "b"
            numB -= 1
    #newsstring"aaabb"
    #"cac"
    while i < len(s):
        if s[i] != ('b'):
            newstring += s[i]
        i += 1
    return newstring


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = smallestString(s)

    fptr.write(result + '\n')

    fptr.close()

"""
Given a string, obtain the alphabetically smallest string possible by swapping either adjacent 'a' and 'b' characters or adjacent 'b' and 'c' characters, any number of times.
 
Note: A string x is alphabetically smaller than a string y if, for the first index i where x and y differ, x[i] < y[i] .
 
Example
s = "abaacbac"
 
The alphabetically smallest possible string is obtained by applying the following operations:
'c' at index 5 is swapped with 'b' at index 6. So "abaacbac" becomes "abaabcac".
Then, 'b' at index 2 is swapped with 'a' at index 3. So "abaabcac" becomes "aababcac".
Finally, 'b' at index 3 is swapped with 'a 'at index 4 to obtain the final answer: "aaabbcac".
 
Function Description
Complete the function smallestString in the editor below.
 
smallestString has the following parameter(s):
    string s:  the given string
Returns:
    string: the lexicographically smallest string obtained after swapping
 
Constraints
1 ≤  length of s ≤ 105
s only contains the characters 'a', 'b', and 'c'.  
"""