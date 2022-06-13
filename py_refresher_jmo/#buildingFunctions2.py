#buildingFunctions2

### don't shadow a variable from an outer scope inside a function! Bad practice!
# don't build a function that is called the same as a python function
# def print():
#     print("Hellow, World!")

# print()


friends = ["rolf","bob"]

def add_friend():
    friend_name = input("Enter your friend name to be added: ")
    friends.append(friend_name)

add_friend()

print(f"Your friends list: {friends}")