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

print(Book.TYPES)