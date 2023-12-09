#smallest among three numbers entered  from user.

one_number = int(input("Enter first Number : "))
second_number = int(input("Enter second Number : "))
third_number = int(input("Enter third Number : "))

if one_number < second_number and one_number < third_number:
    print(f"{one_number}, is the smallest number among {one_number,second_number,third_number} ")
elif second_number<one_number and second_number < third_number:
    print(f"{second_number}, is the smallest number among {one_number,second_number,third_number} ")
elif third_number<one_number and third_number < second_number:
    print(f"{third_number}, is the smallest number among {one_number,second_number,third_number} ")
else:
    ("Enter valid numbers only!!")