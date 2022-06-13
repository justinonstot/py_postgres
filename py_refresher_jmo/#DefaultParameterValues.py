#DefaultParameterValues

myNums = (1,3,4)
# y is default value; x is a REQUIRED parameter
def add(x, y=8):
    print(x + y)

add(x=5)

add = [x*2 for x in myNums]

print(add)