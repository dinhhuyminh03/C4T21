while True:
    txt = input("Enter your name: ")
    if txt.isalpha():
        print("valid name")
        break 
    else:
        print("invalid name")
        
        
        

    # # Ctrl + C
    # if txt.isdigit():
    #     print("Invalid name")
    #     # txt = input("Enter your name again: ")
        
    # else:
    #     print("Valid name")