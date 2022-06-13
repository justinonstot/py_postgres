# args and keyword args. Arbitrary number of each
# def myfunc(a,b):
    # returns 5% of the sum of a and b
    # return sum((a,b))*0.05

# result = myfunc(40,60) # 40 and 60 are POSITIONAL args. 

# print(result)
mynums = [1,2,3]

while True:
    mynums.append(int(input("Enter an integer here: ")))
    cont = input("Do you wish to continue? Y/N ").lower()
    print(mynums)
    if cont == 'y':
        continue
    else:
        break



def myfunc2(*args):
    return (sum(*args)*0.05)

def my_print(*args):
    for item in args:
        print(item)

my_print("thing", "justin", 3, 6)
# result2 = myfunc2(mynums)
# print(f"Your results are in! How about {result2} for an answer?")