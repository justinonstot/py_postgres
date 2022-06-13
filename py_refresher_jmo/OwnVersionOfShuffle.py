#OwnVersionOfShuffle

example = [1,2,3,4,5,6,7]

from random import shuffle

result = shuffle(example)

# print(result)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)
