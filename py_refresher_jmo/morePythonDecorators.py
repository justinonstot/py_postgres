#more python decorators
# functions can be created within other functions
# functions can be passed as arguments to other functions
# Functions can return other functions


def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))
