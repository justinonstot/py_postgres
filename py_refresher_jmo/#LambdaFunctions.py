#LambdaFunctions

# Use sparingly. They can be a PITA to read later.

# No name function, only used to return values, and NOT return actions
# exclusively used to operate on inputs and return an output.

# def add(x, y):
#     return x + y

# print(add(5, 7))

# rewrite above as lambda:
from msilib import sequence


add= lambda x, y: x + y # notice it has no name, so we assign it to a variable called "add" in this case.
print(add(5, 3))
# Notice 4 parts to a lambda function: "lambda" keyword; parameter list; colon; and return values.

# to do the above WITHOUT name, define lambda in the same line where you define it.
print((lambda x, y: x + y)(5,7)) # this is NOT very common usage.

# example common use of lambda without name for "map"


def double(x):
    return x * 2

sequence = [1,3,5,9]

# # 1 way is to use a List Comprehension
# doubled = [double(x) for x in sequence] #using a function call allows for more complex list comprehensions.
# print(doubled)

# 2 let's use   map: Though list comprehension shown above is faster in python.
doubledMap = map(double, sequence) #runs through each element in list "sequence" and runs it for double()

# 3 the third was is with lambda function
### NOTE: this very cumbersome and cryptic.
doubledLambda = [(lambda x: x*2)(x) for x in sequence] 
print(doubledLambda)

# 4 better than just lambda, use map AND lambda
# #must convert map to list in order to print it out.
doubledMapLambda = map(lambda x: x*2, sequence)
print(f"Using Map and Lambda: {list(doubledMapLambda)}") 





