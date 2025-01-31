# correct = email = prashant123@gmail.com
# password = 1234

email = input("Tell me your email")
if '@' in email:
    password = input("Tell me your password")  

    if email == "prashant123@gmail.com" and password == "1234":
        print("Welcome")
    elif email == "prashant123@gmail.com" and password != "1234":
        print("Password is wrong")
        password = input("Tell me password again")
        if password =='1234':
            print("Finally correct")
        else:
            print("Still incorrect")
    else:
        print("Invalid email and password")
else:
    print("Write the correct email")