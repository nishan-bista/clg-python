

grade =int(input("Enter Grade : "))

if grade>=80 and grade<100:
    print(f"You've scored 'A' with marks {grade}")
elif grade>100:
    print("Invalid Marks")
elif grade>60 and grade<80:
    print(f"You've scored 'B' with marks {grade}")
elif grade>50 and grade<60:
    print(f"You've scored 'C' with marks {grade}")
elif grade>45 and grade<50:
    print(f"You've scored 'D' with marks {grade}")
elif grade>25 and grade<45:
    print(f"You've scored 'E' with marks {grade}")
else:
    print("Sorry, You've Failed")
