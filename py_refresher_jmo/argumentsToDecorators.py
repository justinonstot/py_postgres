# argumentsToDecorators

# add *args and **kwargs to the inner functions

## *args:       take an unlimited number of arguments of any type like "10", "True", "Brandon"
## **kwargs:    take any number of KEYWORD arguments like "count=11", "is_authenticated=True", etc.

# Decorator with arguments
from functools import wraps

def my_decorator_func(func):
    
    @wraps(func) 
    def wrapper_func(*args, **kwargs):
        # do something BEFORE the function.
        func(*args, **kwargs)
        # do something AFTER the function.
    return wrapper_func 

@my_decorator_func
def my_func(my_arg):
    '''Example docstring for the function.'''
    pass

# REMEMBER: decorators hide the function they are decorating
# To fix this, you need to use "functools"
print(my_func.__name__)
print(my_func.__doc__)

