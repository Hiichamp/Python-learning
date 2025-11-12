import random

n = random.randint(1,100)
guess = 0
a =-1

while(a!=n):
    guess +=1
    a = int(input("enter correct number : "))
    if(a>n):
        print("Lower Number please")
    else:
        print("Higher Number please")


print(f"the number is correct {n} and for this guess is {guess}")
