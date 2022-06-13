#UnpackingKeywordArguments

## you could actually use whatever variable name you want with "*" and "**", but "args" (*) and kwargs are convention.
## the "**" (double star) collects keyword arguments
## this will unpack named arguments into key:value pairs
# def named(**kwargs):
#     print(kwargs)


# named("Bob", 25)  # returns a dictionary. Bob is key, age is value.

## *args: collect "positional" arguments
## **kwargs: collect "named" arguments.

## 2: You can also unpack a dictionary INTO named arguments.
## 
# def named(name, age):
#     print(name, age)


# details = {"name": "Bob", "age": 25}  # returns a dictionary. Bob is key, age is value.

# named(**details) # unpack dictionary "details" into two named arguments


# def named(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

def both(*args, **kwargs):  # "args, kwargs" is normally used to accept an unlimited number of arguments. 
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)

both(1,3,5,6,8, name="Jim", age=45, gender = 'male') 

## the "args, kwargs" is normally used to accept an unlimited number of arguments.
## this is used so that some or all of those arguments can be passed onto another function: 
## EXAMPLE: 
## ## you have below a post function that takes in a Url, some data, some json and any number of keyword arguments.
## ## returns another function

"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""

def myFunction(**kwargs):
    print(kwargs)
