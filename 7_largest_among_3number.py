#Program to find largest out of three number expected from user.

input_one = int(input("Enter First Number : "))
input_two = int(input("Enter Second Number : "))
input_three = int(input("Enter Third Number : "))

if input_one > input_two and input_three:
    print(f"{input_one} is the Largest among '{input_one}, {input_two}, {input_three}' three number")
elif input_two > input_three and input_one:
    print(f"{input_two} is the Largest among '{input_one}, {input_two}, {input_three}' three number")
elif input_three > input_one and input_two:
    print(f"{input_three} is the Largest among '{input_one}, {input_two}, {input_three}' three number")
else:
    print("Invalid value")