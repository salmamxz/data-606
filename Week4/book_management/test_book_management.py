import unittest

from book_management import (BookManagementSystem, PrintedBook, EBook)


#i am testing the main features of my book management system
class TestBookManagementSystem(unittest.TestCase):

    #i create two books and add them to the system before each test
    def setUp(self):
        self.system = BookManagementSystem()

        self.book = PrintedBook(
            "The Book Thief", "Markus Zusak", "101", 584
        )

        self.ebook = EBook(
            "Atomic Habits", "James Clear", "102", "PDF"
        )

        self.system.add_book(self.book)
        self.system.add_book(self.ebook)

    #i check that a book can be added and found using its isbn
    def test_add_and_find_book(self):
        self.assertEqual(
            self.system.find_book("101"),
            self.book
        )

    #i check that searching for a book that does not exist returns none
    def test_find_missing_book(self):
        self.assertIsNone(
            self.system.find_book("999")
        )

    #i check that borrowing an available book changes its availability
    def test_borrow_book(self):
        result = self.book.borrow_book()

        self.assertEqual(
            result, "Book borrowed successfully."
        )
        self.assertFalse(self.book.is_available)

    #i check that returning a borrowed book makes it available again
    def test_return_book(self):
        self.book.borrow_book()
        result = self.book.return_book()

        self.assertEqual(
            result, "Book returned successfully."
        )
        self.assertTrue(self.book.is_available)

    #i check that a book cannot be borrowed again while unavailable
    def test_borrow_unavailable_book(self):
        self.book.borrow_book()
        result = self.book.borrow_book()

        self.assertEqual(
            result, "Book is not available."
        )

    #i check that printed books and ebooks display their own details
    def test_display_book_details(self):
        self.assertIn(
            "Pages: 584", self.book.display_details()
        )
        self.assertIn(
            "Format: PDF", self.ebook.display_details()
        )

    #i check that the system displays both books correctly
    def test_display_all_books(self):
        books = self.system.display_books()

        self.assertEqual(len(books), 2)
        self.assertIn("The Book Thief", books[0])
        self.assertIn("Atomic Habits", books[1])


#i run the unit tests to check that the features work as expected
if __name__ == "__main__":
    unittest.main()
