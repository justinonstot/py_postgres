menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """


welcome = "Welcome to the programming diary!"




print(welcome)

user_input = input(menu)
while user_input != "3":
    if user_input == "1":
        print("Add new entry...")
    elif user_input == "2":
        print("View entries...")
    else:
        print("\n Invalid option, please try again!")
    user_input = input(menu)
