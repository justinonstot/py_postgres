#FunctionsReturningValues

# INCORRECT ##############################
# def add(x, y):
#     print(x + y)

# add(5, 8)
# result = add(5, 8)
# print(result)
##########################################

# gives 13, 13, None as output
# means "undeclared value"
# when the function finished running, the "result" value = None.
# instead we need to RETURN a value from our function
# functions, by default, return "None".
# so lets return our value, doing it correctly below:

def add(x, y):
    return x + y # the return statement terminates the function. So put it LAST in your function usually.

# add(5, 8)
result = add(5, 8)
print(result)