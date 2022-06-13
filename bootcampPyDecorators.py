# for adding things to existing functions, timers, perf monitor, etc.
# functions can be passed and called to by other functions

def hello(name = 'Jose'):
    print(f"The hello() function has been executed!")

    def greet():
        return '\t This is the greet() function inside hello.'

    def welcome():
        return "\t This is welcome() inside hello!"

    print("I am going to return a function!!!")

    if name == 'Jose':
        return greet
    else:
        return welcome 

# my_new_func = hello('Jose')

# print(my_new_func())

def cool():
    def super_cool():
        return 'I am very cool!'
    
    return super_cool

# some_func = cool()
# print(some_func())

def hello():
    return 'Hi Jose!'

# passing a function as an argument.
def other(some_def_func):
    print(f'Other code runs here!')
    print(some_def_func())

# other(hello)

def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before original function')

        original_func()

        print('Some extra code AFTER the original function')

    return wrap_func

@new_decorator # the @ operator makes all this easier
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()
