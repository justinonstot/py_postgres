# List comprehensions

numbers = [1,3,5]

# double them
doubled_iterator = []
doubled_listcomp = []

for num in numbers:
    doubled_iterator.append(num*2)

print(doubled_iterator)

# list comprehension

doubled_listcomp = [x*2 for x in numbers]

print(doubled_listcomp)


# friends = ["Rolf","Sam","Samantha","Saurabh","Jenn"]
friends = ["Sam","Samantha","Saurabh"]

starts_s = [friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)
print("starts_s: ", id(starts_s))
print("friends: ", id(friends))