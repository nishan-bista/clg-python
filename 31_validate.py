# Validate the email address and password length. check for the presenece of special characters in the password , ensure that both username and password are not empty

user_email = input("Enter Your Email address : ")
user_password = input("Enter Password ")
# email_valid = user_email.endswith("@gmail.com")

password_len = len(user_password)

numbers = 1,2,3,4,5,6,7,8,9,0



if user_email=="" and user_password=="":
    print("email and password empty not allowed")
else:
    if len(user_password)<8:
        print("Password Must be Atleast 8 character long")
    elif "@gmail.com" not in user_email:
        print("Email address is not valid")
    elif "@" not in user_password  and "!" not in user_password and "#" not in user_password and "&" not in user_password and "*" not in user_password:
        print("Password must contain atleast one special character and atleast one Numeric value !")
    else:
        print(f"\nYour Id is : {user_email}\nYour password is : {user_password}")



    

 





