# Errors should be relevant to the program they are related to
# Python errors are very often used for flow control.

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor



# grades = []
grades = [78, 99, 85, 100]
print(len(grades))

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
else:
    # Assuming no error in "try", then do our payload    
    print(f"the average grade is {average}.")
finally:
    print("thanks!")