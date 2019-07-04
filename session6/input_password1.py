while True:
    txt = input("Enter your password: ")
    if txt.isalpha():
        print("Invalid password")
    else:
        print("Valid password")
        break 