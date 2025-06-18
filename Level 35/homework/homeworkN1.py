def login_system():
    authorized = False

    while not authorized:
        log_in = input("Enter your login details: ")
        
        if log_in == "nika123":
            authorized = True
            print("Access granted!")
        else:
            print("Access denied. Try again.")

login_system()