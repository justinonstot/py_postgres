#UnpackingFunctionArgs

## Here we examine variable length arguments.

## EXAMPLE 1:
## collect multiple arguments into a single variable.
# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg

#     return total

# print(multiply(1,3,5,9))

## EXAMPLE 2:
## you can also use the inverse to pass multiple values from list into the function
## must have the same number of parameters in your list as the function accepts.
# def add(x, y):
#     return x + y
# nums = [3, 5]
# print(add(*nums))

## EXAMPLE 3:
# # you can also a dictionary to pass i nvalues:
# def add(x, y):
#     return x + y

# nums = {"x": 15, "y": 25}
# # print(add(*nums.values())) #OR even better:
# print(add(**nums))  #passes in each key as a named argument and value that is associated with the key.

## EXAMPLE 4:
## Use multiple args
def multiply(*args):
    print(f"args provided: {args}")
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*args, operator):  # accepts one or more arguments and then apply the mandatory "operator"
    if operator == "*":
        return multiply(*args) 
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to the apply() function."

print(apply(1,3,6,7, operator="*")) # MUST pass in named argument for "operator"


