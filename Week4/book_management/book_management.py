
from abc import ABC, abstractmethod


# Abstraction: defines the structure of a book
class Book(ABC):

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_available = True

    # Encapsulation: controls access to availability
    @property
    def is_available(self):
        return self._is_available

    def borrow_book(self):
        if self._is_available:
            self._is_available = False
            return "Book borrowed successfully."
        return "Book is not available."

    def return_book(self):
        if not self._is_available:
            self._is_available = True
            return "Book returned successfully."
        return "Book is already available."

    @abstractmethod
    def display_details(self):
        pass


# Inheritance: PrintedBook inherits from Book
class PrintedBook(Book):

    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.pages = pages

    # Polymorphism: displays printed book details
    def display_details(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


# Inheritance: EBook inherits from Book
class EBook(Book):

    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    # Polymorphism: displays ebook details
    def display_details(self):
        return f"{self.title} by {self.author}, Format: {self.file_format}"


class BookManagementSystem:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(book.display_details())


# Main program
system = BookManagementSystem()

book1 = PrintedBook("The Book Thief", "Markus Zusak", "101", 584)
book2 = EBook("Atomic Habits", "James Clear", "102", "PDF")

system.add_book(book1)
system.add_book(book2)

print("BOOK MANAGEMENT SYSTEM")
system.display_books()

print("\nBorrowing a book:")
print(book1.borrow_book())
print("Available:", book1.is_available)
