#Program to read the value of integer m and display the value of N is 1 when M is larger than 0,0 when M is 0 and -1 when M is less than 0.

m_value = int(input("Enter the value of M : "))

if m_value == 0:
    print("The value of N is 0")
elif m_value>0:
    print("The value of N is 1")
else:
    print("The value of N is -1")