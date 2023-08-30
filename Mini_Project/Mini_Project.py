class Library:
    d = {}

    def __init__(self, list_of_book, library_name):
        self.list = list_of_book
        self.library_name = library_name

    def display(self):
        print(f"The available books in {self.library_name} are: ")
        for i in self.list:
            print(i)

    def add_book(self):
        new_books_name = input("Enter the name of new book: ")
        self.list.append(new_books_name)
        print(f"{new_books_name} book has been added.")

    def lend(self):
        lend_book = input("Enter the name of book you lend: ")
        if lend_book in self.list:
            lend_name = input("Enter the name of person who lend this book: ")
            self.list.remove(lend_book)
            self.d[lend_book] = lend_name
            print(f"{lend_book} is lent to {self.d[lend_book]}.")
        elif lend_book in self.d.keys():
            print(f"{lend_book} is already lent to {self.d[lend_book]}.")
        else:
            print(f"The {lend_book} book is not in the library.")

    def return_book(self):
        book_return = input("Enter the name of book returned: ")
        if book_return in self.d.keys():
            print(f"The {book_return} book is returned by {self.d[book_return]}.")
            self.list.append(book_return)
            self.d.pop(book_return)
        else:
            print("The book is already return or you want to add new books.")


emran_library = Library(["Python", "C", "R", "Java"], "Emran_Library")


def main(lib):
    while True:
        user_input = input('''Enter your desired input from below options:
        1. Type display to display all the book available in the library.
        2. Type lend to lend the book.
        3. Type add to add book in library.
        4. Type return to return the book in library
        5. Type exist from the system.
        ''')
        if user_input == "display":
            lib.display()
        elif user_input == "lend":
            lib.lend()
        elif user_input == "add":
            lib.add_book()
        elif user_input == "return":
            lib.return_book()
        elif user_input == "exist":
            break
        else:
            print("Please choose one option that is mention below.")


main(emran_library)
