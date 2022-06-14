menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """


welcome = "Welcome to the programming diary!"

entries = [
    {"content": "Today I started learning python", "date": "2020-01-01"},
    {"content": "I create my first database", "date": "2020-02-01"},
    {"content": "I finished writing my programming diary app", "date": "2020-03-01"},
    {"content": "I finished writing my prog diary today!", "date": "2020-04-01"},
    {"content": "Today I'm continuing my learning on programming", "date": "2020-04-02"},
] 

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
