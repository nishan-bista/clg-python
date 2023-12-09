#To check a number is positive or negetive

number = int(input("Enter a Number to check : "))

if number <0:
    print(f"{number} is a Negetive Number")
elif number==0:
    print(f"{number} It is Neutral Number")
else:
    print(f"{number} is a Positive Number")
