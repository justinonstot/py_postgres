# variables: names for values
x = 15 # 15 is referred to as 'x' here.

print(x)

y = "mystring"
print(y[1]*2)

y = y*2

print(y)

z1 = y

# these will be the same object
print(id(y))
print(id(z1))

# these will be different
z1 = y*2
print(id(y))
print(id(z1))


# format strings aka 'f' strings.
name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

# template strings
name = "Bob"
greeting = "Hello, {}"

with_name = greeting.format(name)
print(with_name)

# create longer template string
longer_phrase = "Hello, {}. Today is {}"

print(longer_phrase.format(name,"Monday"))

### getting user input:
#name = input("Enter your name: ")
#print(name)

    # with math
size_input = input("How big is your house (in sq ft): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f"{square_feet} square_feet is equal to {square_meters:.2f} square meters")

