#another try at understanding decorators

# without the "at" syntax
def decorator_func_logger(target_func): # this is the "decorator" function.
    def wrapper_func():
        print("Before calling", target_func.__name__)
        target_func()
        print("After calling", target_func.__name__)

    return wrapper_func

def target():
    print("Python is in the decorated target function")

dec_func = decorator_func_logger(target)
dec_func()


# Using syntactic sugar, we can simplify the decorator function


def decorator_func_logger2(target_func2): # this is the "decorator" function.
   def wrapper_func2():
        print("Before calling", target_func2.__name__)
        target_func2()
        print("After calling", target_func2.__name__)

   return wrapper_func2

@decorator_func_logger2
def target():
    print("Python is in the decorated target function")

target()