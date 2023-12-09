#Program to check wheather it is alphabet or number.

user =input("Enter anything : ")
a = user.isalpha()
b = user.isdigit()

if a is True:
    print("It is an alphabet!")
elif b is True:
    print("It is a number!")
else:
    print("It is not alphabet nor number ")