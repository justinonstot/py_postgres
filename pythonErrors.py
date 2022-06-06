# Errors should be relevant to the program they are related to
# Python errors are very often used for flow control.

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor



grades = [78, 99, 85, 100]
print(len(grades))

print("Welcome to the average grade program.")
average = divide(sum(grades), len(grades))

print(f"the average grade is {average}.")