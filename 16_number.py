#program to whether a number is divisible by 2 and 3 both

user_input = int(input("Enter Number : "))
a = user_input % 2
b = user_input % 3

if user_input == 0:
    print("infinite")
elif a == 0 and b ==0:
    print(f"{user_input}, The number is divisible by both.")
elif a== 0 and b != 0:
    print(f"{user_input}, The number is divisible by 2 only.")
elif b== 0 and a != 0:
    print(f"{user_input}, The number is divisible by 3 only.")
else:
    print(f"{user_input}, is not divisible by both")
