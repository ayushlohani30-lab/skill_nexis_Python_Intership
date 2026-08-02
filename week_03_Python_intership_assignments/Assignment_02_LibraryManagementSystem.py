# Library Management System using Object-Oriented Programming

class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"ID: {self.book_id:<5} | Title: {self.title:<25} | Author: {self.author:<18} | Status: {status}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id in self.books:
            print(f"Book with ID {book_id} already exists.")
            return
        new_book = Book(book_id, title, author)
        self.books[book_id] = new_book
        print(f"Book '{title}' added successfully!")

    def remove_book(self, book_id: str):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Book '{removed.title}' removed from library.")
        else:
            print(f"No book found with ID {book_id}.")

    def issue_book(self, book_id: str):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.is_issued:
                book.is_issued = True
                print(f"Book '{book.title}' has been issued successfully.")
            else:
                print(f"Sorry, '{book.title}' is already issued.")
        else:
            print(f"No book found with ID {book_id}.")

    def return_book(self, book_id: str):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_issued:
                book.is_issued = False
                print(f"Book '{book.title}' returned successfully.")
            else:
                print(f"'{book.title}' was not marked as issued.")
        else:
            print(f"No book found with ID {book_id}.")

    def display_all_books(self):
        if not self.books:
            print("The library currently has no books.")
        else:
            print(f"\n=== {self.name.upper()} CATALOG ===")
            for book in self.books.values():
                print(book)


def main():
    lib = Library("Central City Library")

    # Pre-populating some initial books
    lib.add_book("101", "Clean Code", "Robert C. Martin")
    lib.add_book("102", "Python Crash Course", "Eric Matthes")

    while True:
        print("\n=== LIBRARY MANAGEMENT MENU ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            b_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            lib.add_book(b_id, title, author)
        elif choice == '2':
            b_id = input("Enter Book ID to remove: ").strip()
            lib.remove_book(b_id)
        elif choice == '3':
            b_id = input("Enter Book ID to issue: ").strip()
            lib.issue_book(b_id)
        elif choice == '4':
            b_id = input("Enter Book ID to return: ").strip()
            lib.return_book(b_id)
        elif choice == '5':
            lib.display_all_books()
        elif choice == '6':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()