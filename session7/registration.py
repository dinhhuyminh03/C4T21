print("Create a account")
name = input("Enter your username: ")
while True:
    password= input("Enter your password: ")
    if len(password) < 8:
        print("Password must be at least 8 letters ")
    elif password.isalpha():
        print("Invalid password !")
    elif password.isdigit():
        print("Invalid password !")
    else:
        password_1= input("Enter your password again: ")
        break 
if password == password_1:
    email = input("Enter your email: ")
    if "@" in email:
        print("Account created !")
    else:
        email=input("Enter your email: ")
print ("Account created !")

# while True:
#     if password == password_1:
#         email = input("Enter your email: ")
#         if "@" in email:
#             print("Account created !")
#         else:
#             email = input("Enter your email: ")
#     else:
#         print("Invalid password !")
#         password_1= input("Enter your password again: ")
#         if password == password_1:
#             email = input("Enter your email: ")
#     break 
# print("Account created !")
    
    

    


