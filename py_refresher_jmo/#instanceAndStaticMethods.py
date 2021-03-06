#instanceAndStaticMethods

class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod      # class method gets the class (cls) when called
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod     # these methods don't get anything when you call them
    def static_method():
        print("Called static method")

class Book:
    TYPES = ("hardcover", "paperback") 

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight} grams>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    ## NOTE: "book" and "cls" are both the class. They are interchangeable.
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

## How do I make sure I can only pass in hardcover or paperback instead of any string?
## by creating a "factory" in the class above.
book = Book.hardcover("Harry Glover",  1500)
softBook = Book.paperback("Jimmy John", 1400)

print(book)
print(softBook)