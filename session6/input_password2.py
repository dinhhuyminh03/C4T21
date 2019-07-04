while True:
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password must be at least 8 letters ")
    elif password.isalpha():
        print("Password must contain numbers")
    else:
        print("Valid password !")
        break
