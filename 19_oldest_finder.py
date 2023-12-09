
#9 Accept the age of 4 people and display the oldest one.


first_age = int(input("Enter the age of First person : "))
second_age = int(input("Enter the age of Second person : "))
third_age = int(input("Enter the age of Third person : "))
fourth_age = int(input("Enter the age of Fourth person : "))

if first_age>second_age and first_age>third_age and first_age>fourth_age:
    print(f"{first_age}, Is the oldest among {first_age,second_age,third_age,fourth_age}")
elif second_age>first_age and second_age>third_age and second_age>fourth_age:
    print(f"{second_age}, Is the oldest among {first_age,second_age,third_age,fourth_age}")
elif third_age>first_age and third_age>second_age and third_age>fourth_age:
    print(f"{third_age}, Is the oldest among {first_age,second_age,third_age,fourth_age}")
elif fourth_age>first_age and fourth_age>second_age and fourth_age>third_age:
    print(f"{fourth_age}, Is the oldest among {first_age,second_age,third_age,fourth_age}")
else:
    print("The age you've Entered is Invalid!!")