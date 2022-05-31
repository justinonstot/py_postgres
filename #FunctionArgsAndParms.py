#FunctionArgsAndParms

def add(x, y): # x and y are parameters
    pass

add(1,2) #1 and 2 are arguments

def say_hello_none(): #function with NO parameters.
    print("Hello!")

# say_hello("bob") #wouldnlt work! say_hello() has no parameters defined.



def say_hello(name, surname): #function with NO parameters.
    print(f"Hello, {name} {surname}!")


say_hello(surname = "Justin", name = "Onstot") # named or keyword arguments. Make things clear!

# def divide(numerator, denominator):
#     if denominator != 0:
#         print(numerator / denominator)
#     else:
#         print("You fool! You can not divide by zero! ")

# divide(numerator = 12, denominator=0)

def divide(numerator, denominator):
    if denominator != 0:
        return numerator / denominator
    else:
        return "You are a mathematical idiot and should be banned from computer use!"

result = divide(10, 0)
print(result)
