
import json
import os

FILE_NAME = "library.json"


class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued


class Library:
    def __init__(self):
        self.books = {}
        self.load_books()

    def load_books(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                for bid, info in data.items():
                    self.books[bid] = Book(
                        bid, info["title"], info["author"], info["issued"])

    def save_books(self):
        data = {}
        for bid, book in self.books.items():
            data[bid] = {
                "title": book.title,
                "author": book.author,
                "issued": book.issued
            }
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def add_book(self):
        bid = input("Enter Book ID: ")
        if bid in self.books:
            print("Book already exists.")
            return
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        self.books[bid] = Book(bid, title, author)
        self.save_books()
        print("Book added successfully.")

    def search_book(self):
        keyword = input("Search by title or author: ").lower()
        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                status = "Issued" if book.issued else "Available"
                print(book.book_id, book.title, book.author, status)

    def issue_book(self):
        bid = input("Enter Book ID to issue: ")
        if bid in self.books and not self.books[bid].issued:
            self.books[bid].issued = True
            self.save_books()
            print("Book issued.")
        else:
            print("Book not available.")

    def return_book(self):
        bid = input("Enter Book ID to return: ")
        if bid in self.books and self.books[bid].issued:
            self.books[bid].issued = False
            self.save_books()
            print("Book returned.")
        else:
            print("Invalid operation.")

    def show_report(self):
        total = len(self.books)
        issued = sum(1 for b in self.books.values() if b.issued)
        print("Total Books:", total)
        print("Issued Books:", issued)


def main():
    library = Library()
    while True:
        print("\n1.Add 2.Search 3.Issue 4.Return 5.Report 6.Exit")
        choice = input("Choose option: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.search_book()
        elif choice == "3":
            library.issue_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.show_report()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


main()