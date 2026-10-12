from abc import ABC, abstractmethod


class Book(ABC):

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_available = True

    # Check whether the book is available or not
    @property
    def is_available(self):
        return self._is_available

    #borrow a book if it is available
    def borrow_book(self):
        if self._is_available:
            self._is_available = False
            return "Book borrowed successfully."
        return "Book is not available."

    #return the borrowed book
    def return_book(self):
        if not self._is_available:
            self._is_available = True
            return "Book returned successfully."
        return "Book is already available."

    #each book is displayed with its details
    @abstractmethod
    def display_details(self):
        pass


#printed book
class PrintedBook(Book):

    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.pages = pages

    def display_details(self):
        return (
            f"Title: {self.title} | Author: {self.author} | "
            f"ISBN: {self.isbn} | Pages: {self.pages}"
        )


#e book
class EBook(Book):

    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def display_details(self):
        return (
            f"Title: {self.title} | Author: {self.author} | "
            f"ISBN: {self.isbn} | Format: {self.file_format}"
        )


#book present on the platform
class BookManagementSystem:

    def __init__(self):
        self.books = []

    #add a book to the platform
    def add_book(self, book):
        self.books.append(book)

    #find book using isbn
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    #display book details
    def display_books(self):
        return [book.display_details() for book in self.books]


























if __name__ == "__main__":
    system = BookManagementSystem()

    book1 = PrintedBook(
        "The Book Thief", "Markus Zusak", "101", 584
    )
    book2 = EBook(
        "Atomic Habits", "James Clear", "102", "PDF"
    )

    system.add_book(book1)
    system.add_book(book2)

    print("BOOK MANAGEMENT SYSTEM")
    print("----------------------")

    for details in system.display_books():
        print(details)

    print("\nBorrowing a book:")
    print(book1.borrow_book())
    print("Available:", book1.is_available)
