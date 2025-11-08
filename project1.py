import random

computer = random.choice([1,-1,0])
yourChoice = input("enter your number : ")

youPred = {"s":1,"w":-1,"g":0}
revPred = {1:"snake",-1:"water",0:"Gun"}

you = youPred[yourChoice]

print(f"you choose {revPred[you]}\n computer choose {revPred[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == 1 and you == -1 ):
        print("you lose")
    
    elif(computer == 0 and you == -1 ):
        print("you win")

    elif(computer == 1 and you == 0 ):
        print("you win")   

    elif(computer == -1 and you == 1 ):
        print("you win") 

    elif(computer == 0 and you == 1 ):
        print("you lose")

    elif(computer == -1 and you == 0 ):
        print("you lose")    


 
#    the shortest program ever is means this total if and else of the shortest code is --- 

    # if(computer - you == -1 or computer - you == 2 ):
    #     print("you lose")
    
    # else:
    #     print("you win")
