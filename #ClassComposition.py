#ClassComposition

## Composition is used ALOT
## Class that contains many classses...
## For instance a Bookshelf has many Books.

class BookShelf:
    def __init__(self, *books):
        self.books = books 
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
       self.name = name

    def __str__(self):
        return f"Book {self.name}" 

book = Book("Harry Potter")
book2 = Book("Pride and Prejudice")
shelf = BookShelf(book, book2)

print(shelf)

## It makes no sense to make a Book class inherit from Bookshelf... a Book is not a bookshelf.
## instead, a bookshelf "HAS" many books.
## instead put a constructor in above class to allow it to take in the count of books.
