def bank_system():
    names = []
    passwords = []
    balances = []

    while True:
        print("\n==== Bank Menu ====")
        print("1. Create account")
        print("2. Log in")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Enter username: ")
            if name in names:
                print("This name already exists.\n")
            else:
                password = input("Enter password: ")
                names.append(name)
                passwords.append(password)
                balances.append(0)
                print("Account created!\n")

        elif choice == "2":
            name = input("Enter username: ")
            password = input("Enter password: ")

            found = False

            for i in range(len(names)):
                if names[i] == name and passwords[i] == password:
                    print("Login successful!\n")
                    found = True

                    while True:
                        print("---- Account Menu ----")
                        print("1. Check balance")
                        print("2. Deposit money")
                        print("3. Withdraw money")
                        print("4. Log out")

                        choice = input("Choose: ")

                        if choice == "1":
                            print("Your balance is:", balances[i], "GEL\n")

                        elif choice == "2":
                            amount = input("Enter amount: ")
                            try:
                                amount = int(amount)
                                balances[i] += amount
                                print("Deposit successful.\n")
                            except:
                                print("Please enter a number!\n")

                        elif choice == "3":
                            amount = input("Enter amount: ")
                            try:
                                amount = int(amount)
                                if amount <= balances[i]:
                                    balances[i] -= amount
                                    print("Withdrawal successful.\n")
                                else:
                                    print("Not enough balance!\n")
                            except:
                                print("Please enter a number!\n")

                        elif choice == "4":
                            print("Logged out.\n")
                            break
                        else:
                            print("Invalid choice.\n")
                    break

            if found == False:
                print("Wrong username or password.\n")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

bank_system()