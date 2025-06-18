def to_do_list_app():
    to_do_list = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View list")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        print("-------------------")

        choice = input("Enter a number: ")

        if choice == "1":
            if len(to_do_list) == 0:
                print("-------------------")
                print("The list is empty.")
            else:
                print("\nTasks:")
                i = 0
                while i < len(to_do_list):
                    print(str(i + 1) + ". " + to_do_list[i])
                    i += 1

        elif choice == "2":
            print("-------------------")
            task = input("Enter a new task: ")
            to_do_list.append(task)
            print("Added!")

        elif choice == "3":
            print("-------------------")
            if len(to_do_list) == 0:
                print("The list is empty.")
            else:
                print("Tasks:")
                i = 0
                while i < len(to_do_list):
                    print(str(i + 1) + ". " + to_do_list[i])
                    i += 1
                number = input("Which one to remove? (number): ")
                number = int(number)

                if number >= 1 and number <= len(to_do_list):
                    new_list = []
                    i = 0
                    while i < len(to_do_list):
                        if i != number - 1:
                            new_list.append(to_do_list[i])
                        i += 1
                    to_do_list = new_list
                    print("Removed!")
                else:
                    print("Invalid number.")

        elif choice == "4":
            print("-------------------")
            print("Program ended.")
            break

        else:
            print("Enter a valid number (1-4).")

to_do_list_app()