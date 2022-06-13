#interactionsBetweenFunctions

from random import shuffle
import functools

# shuffle list
example = [1,2,3,4,5,6,7]

def add_line_decorator(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        print("-" * 30)
        mything = func(*args, **kwargs)
        return mything
    return wrapper_func

@add_line_decorator
def run_shuffle(x):
    shuffle(x)
    return f"The shuffled list is: {x}"

# @add_line_decorator
# def print_thing(x):
#     return f"the thing to print is {x}"

print(run_shuffle([2,3,4,5,6,7,8]))
# print(f"Example BEFORE shuffle: {example}")
# print(print_thing("good"))

