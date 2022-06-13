#first class functions
# functions in python are just variables that happen to be callable.
# but they are no different from other values.


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide) # example of using a first-class function
print(result)