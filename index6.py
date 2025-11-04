# if,else,elif use in python

# a = int(input("Enter your age : "))

# if(a>=18):
#     print("you are eligible for vote")  

# else:
#     print('you are not eligible')



# a1 = int(input("enter your a1 marks :"))
# a2 = int(input("enter your a2 marks :"))
# a3 = int(input("enter your a3 marks :"))
# a4 = int(input("enter your a4 marks :"))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("winner is a1 ",a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("winner is a2 ",a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("winner is a3 ",a3)


# elif(a4>a1 and a4>a2 and a4>a3):
#     print("winner is a4 ",a4)


# print("congrates")

marks1 = int(input("enter your marks1 :"))
marks2 = int(input("enter your marks2 :"))
marks3 = int(input("enter your marks3 :"))




pt = (100 *(marks1 + marks2 + marks3))/300

if(pt>=33 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed",pt)


else:
    print("you are failed"  )