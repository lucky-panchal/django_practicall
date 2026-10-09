class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"ID: {self.book_id}, Title: {self.title}, "
              f"Author: {self.author}, Status: {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Inventory:")
            for book in self.books:
                book.display()

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")


# Creating a Library object
library = Library()

# Adding books
library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Alice Brown"))
library.add_book(Book(103, "Computer Networks", "David Lee"))

# Display inventory
library.display_books()

# Issue a book
library.issue_book(101)

# Display inventory after issuing
library.display_books()

# Return the book
library.return_book(101)

# Display inventory after returning
library.display_books()