#Program to check whether a number is divisible by 3 or not.
user_input = int(input("Enter a Number : "))
b = user_input % 3
if b == 0:
    print(f"{user_input}, is divisible by 3")
else:
    print(f"{user_input}, is not divisible by 3")