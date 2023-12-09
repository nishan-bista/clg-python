#5 check whether the user input is even or odd and display it to user.


user_input = int(input("Enter a number to check even or odd : "))

x = user_input % 2

if x==0:
    print(f"{user_input}, It is even Number.")
else:
    print(f"{user_input}, It is odd Number.")