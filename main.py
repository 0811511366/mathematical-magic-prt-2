#check for prime numbers
from math import sqrt

number=int(input("enter a number to check: "))
print("\n")

if number>1:
    for i in range(2,int(sqrt(number))+1):
        if(number%i)==0:
            print(f"{number} is not a prime")
            break
    else:
        print(f"{number} is a prime")
else:
    print(f"{number} is not a prime")