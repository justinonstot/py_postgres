#ClassComposition

## Composition is used ALOT

class BookShelf:
    def __init__(self, quantity):
        self.quantity = quantity
    
    def __str__(self):
        return f"Bookshelf with {self.quantity} books."


shelf = BookShelf(300)

print(shelf)