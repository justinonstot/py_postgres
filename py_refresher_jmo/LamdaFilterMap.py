#LamdaFilterMap
# you don't CALL the functions inside map, you just pass the name. 

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

# instead of for loop, lets use map to apply "square" function to each item in list:
for item in map(square, my_nums):
    print(item)

# if we want a new list, use "list"
print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']

even_names = list(map(splicer, names))
print(even_names)

# Filter function; returns true or false for each item.Filter based off the functions condition
# function must return boolean
def check_even(num):
    return num%2 ==0

myNums = [1,2,3,4,5,6]

filteredList = list(filter(check_even, myNums))

print(filteredList)

# Lambda expressions: Convert one of the functions to this.
# def square(num):
#     return num ** 2

# print(square(3))
# Same as above "square" function, but as a lambda

## We mostly use lambda with map and filter.
## Instead of wasting space defining full function "square", lets just map and lambda
print(list(map(lambda num: num ** 2, myNums)))

## Let do the same with "filter", turning "check_even" filter func to lambda/filter:
filter(lambda num: num%2 == 0, myNums)
onlyEvens = filter(lambda num: num%2 == 0, myNums) 
print(list(onlyEvens))

words = ('blah','going','nowhere') 
mystuff = list(map(lambda words: words.upper(), words))

print(mystuff)