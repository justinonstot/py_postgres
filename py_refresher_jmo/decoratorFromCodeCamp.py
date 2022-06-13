# Decorator stuff from freeCodeCamp.org
# https://www.freecodecamp.org/news/python-decorators-explained-with-examples/

# use a decorator when you need to change the behavior of a function 
# without modifying the function itself.

# like add logging, performance test, caching, permissions verification

# Remember:  a function is an OBJECT. A function can be assigned to a variable

def printme(x):
    return print(f"my value is {x}")

# assign without the parentheis since we dont want to execute the func right now.
myfunc_call = printme

# The function can be accessed from that variable.
print(type(myfunc_call))


# # a function can be nested in another function
# def outer_function():
#     def inner_function():
#         print('I came from the inner function')

#     # execute the inner function from inside the outer function.
#     inner_function()

# outer_function()

# the inner_function is NOT availble outside of the outer_function.

# since a function can be nested inside another function it can be returned.
def outer_function():
    '''Assign task to student'''

    task = 'Read Python book Chapter 3'
    def inner_function():
        print(task)
    return inner_function # here outer_function is "returning" inner function

homework = outer_function()
homework() #returns "Read Python book Chapter 3" 

####################################################################
# a function can be passed to another function as an argument:
####################################################################
def friendly_reminder(func):
    '''Reminder for husband'''

    func()
    print(f"Don't forget to bring your wallet!")

def action():
    print(f"I am going to the store to buy you something nice!")

