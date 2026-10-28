"""A simple library using a base class and a Book subclass."""

from datetime import date


class LibraryItem:
    """Common information shared by items in a library."""

    def __init__(self, title):
        self.title = title

    def display_info(self):
        print(f"Library item: {self.title}")


class Book(LibraryItem):
    """A book is a kind of library item."""

    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
        self.is_issued = False
        self.issued_on = None

    def display_info(self):
        # Overriding this method is an example of polymorphism.
        status = "issued" if self.is_issued else "available"
        print(f"Book: {self.title} by {self.author} ({status})")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title in self.books:
            raise ValueError("A book with that title is already in the library.")
        self.books[book.title] = book

    def remove_book(self, title):
        book = self._find_book(title)
        if book.is_issued:
            raise ValueError("Return the book before removing it.")
        del self.books[title]

    def issue_book(self, title):
        book = self._find_book(title)
        if book.is_issued:
            raise ValueError("That book is already issued.")
        book.is_issued = True
        book.issued_on = date.today()
        print(f"Issued '{title}' on {book.issued_on}.")

    def return_book(self, title):
        book = self._find_book(title)
        if not book.is_issued:
            raise ValueError("That book was not issued.")
        book.is_issued = False
        book.issued_on = None
        print(f"Returned '{title}'.")

    def show_books(self):
        if not self.books:
            print("The library has no books yet.")
            return
        for book in self.books.values():
            book.display_info()

    def _find_book(self, title):
        if title not in self.books:
            raise ValueError("Book not found.")
        return self.books[title]


def main():
    library = Library()
    # Starter books make the example ready to use.
    library.add_book(Book("The Hobbit", "J. R. R. Tolkien"))
    library.add_book(Book("Matilda", "Roald Dahl"))

    while True:
        print("\nLIBRARY: 1 Show books  2 Add  3 Remove  4 Issue  5 Return  0 Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                library.show_books()
            elif choice == "2":
                title = input("Book title: ").strip()
                author = input("Author: ").strip()
                library.add_book(Book(title, author))
                print("Book added.")
            elif choice == "3":
                library.remove_book(input("Book title: ").strip())
                print("Book removed.")
            elif choice == "4":
                library.issue_book(input("Book title: ").strip())
            elif choice == "5":
                library.return_book(input("Book title: ").strip())
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Please choose one of the listed numbers.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
