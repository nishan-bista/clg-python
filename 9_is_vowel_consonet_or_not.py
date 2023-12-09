#To check it is vowel or consonent.

user_input = input("Enter a charecter to check it is vowel or consonent : ")
vowel ="aeiou"
consonent ="abcdfghjklmnpqrstvwxyz"
if user_input in vowel:
    print(f"{user_input}, it is vowel ")
elif user_input in consonent:
    print(f"{user_input}, is consonent ")
else:
    print("Enter only vowel or consonent letters!")

