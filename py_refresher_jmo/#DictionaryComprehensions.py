#DictionaryComprehensions

# Like List Comprehension, but we get a dictionary at the end, so key:value pairs

# First step, lets assign index 1 (username) as key

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

username_mapping = {user[1]: user for user in users} #dict comprehension

# print(username_mapping["Bob"]) #returns the username as key, and the entire tuple as value

# have users login

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# get user info tuple, unpack (destructure). the underscore "_" variable is because we don't care about Id.
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct.")
else:
    print("Your details are incorrect.")

