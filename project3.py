import random

n = random.randint(0,11)



a=-1
guess = 0

while(a!=n and guess <3):
    guess +=1
    a = int(input("enter correct number : "))

    if(a==n):
        print(f"you got the number {n} and you attempt is {guess}")
        break
    elif(a>n):
        print("Lower Number please")
    else:
        print("Higher Number please")

if(a!=n):
  print(f"sorry you have only {guess} limit, try again")




