def myFunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print(f"I did not find any fruit here.")

myFunc(blog='apple', fruit='pear')