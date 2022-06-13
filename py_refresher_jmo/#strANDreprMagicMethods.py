#strANDreprMagicMethods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  #this will turn our object into a string for viewing.
         return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

# python automatically calls the __init__ method for us when we instantiate the Person class from above.
bob = Person("Bob", 35)
print(bob)     #python prints out string representation of the object.
