# Library Management System
# This program implements a basic library system where members can borrow and return books

class Book:
    """
    Book class to represent a book in the library
    Attributes:
        title: Name of the book
        author: Author of the book
        is_borrowed: Boolean to track if book is currently borrowed
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # When book is created, it's not borrowed
    
    def mark_as_borrowed(self):
        """Mark the book as borrowed"""
        self.is_borrowed = True
    
    def mark_as_returned(self):
        """Mark the book as returned"""
        self.is_borrowed = False
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"

class LibraryMember:
    """
    LibraryMember class to represent a library member
    Attributes:
        name: Name of the member
        member_id: Unique ID for the member
        borrowed_books: List to store books borrowed by the member
    """
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # Empty list to store borrowed books
    
    def borrow_book(self, book):
        """
        Attempt to borrow a book
        Returns True if successful, False if book is already borrowed
        """
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book):
        """
        Return a borrowed book
        Returns True if successful, False if book wasn't borrowed by this member
        """
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            return True
        return False
    
    def list_borrowed_books(self):
        """Display all books currently borrowed by the member"""
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"- {book}")

# Main program to demonstrate the library system
def main():
    # Create some books
    books = [
        Book("Python Programming", "John Smith"),
        Book("Data Structures", "Jane Doe"),
        Book("Algorithms", "Bob Wilson")
    ]
    
    # Create a library member
    member = LibraryMember("Mohamed Mumin", "M001")
    
    while True:
        # Display menu
        print("\n=== Library Management System ===")
        print("1. List all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View my borrowed books")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            print("\nAvailable Books:")
            for i, book in enumerate(books, 1):
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"{i}. {book} - {status}")
                
        elif choice == '2':
            print("\nAvailable Books:")
            available_books = [b for b in books if not b.is_borrowed]
            for i, book in enumerate(available_books, 1):
                print(f"{i}. {book}")
            
            if available_books:
                try:
                    book_index = int(input("Enter book number to borrow: ")) - 1
                    if 0 <= book_index < len(available_books):
                        if member.borrow_book(available_books[book_index]):
                            print("Book borrowed successfully!")
                        else:
                            print("Sorry, book is already borrowed.")
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No books available to borrow.")
                
        elif choice == '3':
            if member.borrowed_books:
                print("\nYour Borrowed Books:")
                for i, book in enumerate(member.borrowed_books, 1):
                    print(f"{i}. {book}")
                try:
                    book_index = int(input("Enter book number to return: ")) - 1
                    if 0 <= book_index < len(member.borrowed_books):
                        member.return_book(member.borrowed_books[book_index])
                        print("Book returned successfully!")
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("You have no books to return.")
                
        elif choice == '4':
            member.list_borrowed_books()
            
        elif choice == '5':
            print("Thank you for using the Library Management System!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Run the program if this file is run directly
if __name__ == "__main__":
    main()
