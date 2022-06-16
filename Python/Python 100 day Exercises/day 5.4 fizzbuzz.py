#for anything divisbile by 3 = fizz
#for anything divisible by 5 = buzz
#for anything divisibile by both = fizz buzz

from bdb import Breakpoint


Count=100
divthree = (Count % 3)
print(divthree)
divfive = (Count % 5)
print(divfive)
for Count in range(100):
    
    if divfive and divthree ==0:
        Count -= 1
        print("fizzbuzz")
    elif divthree == 0:
        print("fizz")
        Count -= 1
    elif divfive == 0:
        print("buzz")
        Count -=1
    
else:
    print(Count)
    Count=0
    
