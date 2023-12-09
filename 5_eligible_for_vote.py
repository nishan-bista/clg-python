#To check whether the candidate is eligible to vote or not

user_age = int(input("Enter Your Age! : "))
if user_age<0:
    print("Enter Valid Age!!")
elif user_age<18:
    print(f" You're just {user_age}y/o, Not eligible to vote!")
    
else:
    print(f" You're {user_age}y/o, And eligible to vote!")