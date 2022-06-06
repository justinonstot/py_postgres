# Custom Error Classes

# simple Book class that allows me to create new books.
class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages: int):
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")