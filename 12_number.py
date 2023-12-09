#Program to display "Hello" if a number entered by user is a multiple of five, otherwise print"Bye".

user_input = int(input("Enter number : "))
b = user_input % 5
if b == 0:
    print("Hello!")
else:
    print("Bye!")