class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Default: Book is available

    def borrow(self):
        """Mark the book as borrowed if available."""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True  # Successful borrow
        return False  # Book already borrowed

    def return_book(self):
        """Mark the book as available again."""
        self.is_borrowed = False

    def display_info(self):
        """Display book details."""
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f" {self.title} by {self.author} - {status}")


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []  # List of books borrowed by the patron

    def borrow_book(self, book):
        """Attempt to borrow a book from the library."""
        if book.borrow():
            self.borrowed_books.append(book)
            print(f" {self.name} borrowed '{book.title}'.")
        else:
            print(f" Sorry, '{book.title}' is already borrowed.")

    def return_book(self, book):
        """Return a book to the library."""
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f" {self.name} returned '{book.title}'.")
        else:
            print(f" {self.name} doesn't have '{book.title}' to return.")

    def list_borrowed_books(self):
        """List all borrowed books by the patron."""
        if self.borrowed_books:
            print(f"\n {self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                book.display_info()
        else:
            print(f"\n {self.name} has no borrowed books.")


class Library:
    def __init__(self):
        self.books = []  # List of books in the library

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f" Added '{book.title}' to the library.")

    def display_books(self):
        """Show all books in the library with their availability status."""
        if not self.books:
            print("\n No books available in the library.")
            return
        print("\n Library Books:")
        for book in self.books:
            book.display_info()

    def search_book(self, title):
        """Find a book by title in the library."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


def main():
    library = Library()

    while True:
        print("\nLibrary System Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Add Patron")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. List Borrowed Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                book.display_info()
            else:
                print("Book not found.")

        elif choice == '4':
            name = input("Enter patron name: ")
            patron_id = input("Enter patron ID: ")
            patron = Patron(name, patron_id)
            print(f"Patron {name} added with ID {patron_id}.")

        elif choice == '5':
            patron_name = input("Enter patron name: ")
            book_title = input("Enter book title to borrow: ")
            patron = next((p for p in patrons if p.name == patron_name), None)
            book = library.search_book(book_title)
            if patron and book:
                patron.borrow_book(book)
            else:
                print("Patron or book not found.")

        elif choice == '6':
            patron_name = input("Enter patron name: ")
            book_title = input("Enter book title to return: ")
            patron = next((p for p in patrons if p.name == patron_name), None)
            book = library.search_book(book_title)
            if patron and book:
                patron.return_book(book)
            else:
                print("Patron or book not found.")

        elif choice == '7':
            patron_name = input("Enter patron name: ")
            patron = next((p for p in patrons if p.name == patron_name), None)
            if patron:
                patron.list_borrowed_books()
            else:
                print("Patron not found.")

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    patrons = []
    main()