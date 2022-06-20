def FirstFactorial(num):
  number =int(num)
  # create a variable that can be multiplied (not 0)
  factoral = 1 
  #create a while loop of num !=0
  while number != 1:
  #subtract num until it hits 0 
    factoral *= number
  # for each number subrtracted multiply it till the loop ends.
    number -= 1
  # code goes here
  return factoral

# keep this function call here 
print(FirstFactorial(input()))