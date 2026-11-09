3
"""Challenge 3: Library book viewer, borrowing and returns."""

import csv
from dataclasses import dataclass
from pathlib import Path

BOOKS_FILE = Path(__file__).with_name("bookData.txt")


@dataclass
class Book:
    title: str
    author: str
    pages: int
    ID: str
    borrowed: bool = False

    def display(self):
        status = "Borrowed" if self.borrowed else "Available"
        print(f"ID: {self.ID} | {self.title} by {self.author} "
              f"| {self.pages} pages | {status}")


def parse_borrowed(value):
    value = value.strip().lower()
    if value in ("true", "yes", "1", "borrowed"):
        return True
    if value in ("false", "no", "0", "available", ""):
        return False
    raise ValueError(f"Unrecognised borrowing status: {value}")


def load_books():
    books = []
    with BOOKS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        for line_number, row in enumerate(csv.reader(file), start=1):
            if not row or not any(field.strip() for field in row):
                continue
            if row[0].strip().lower() == "title":
                continue  # Ignore a header row if the file has one.
            if len(row) not in (4, 5):
                print(f"Skipping row {line_number}: expected 4 or 5 fields.")
                continue
            try:
                title, author, pages, book_id = (value.strip() for value in row[:4])
                if not title or not author or not book_id:
                    raise ValueError("missing title, author or ID")
                pages = int(pages)
                if pages < 1:
                    raise ValueError("pages must be positive")
                borrowed = parse_borrowed(row[4]) if len(row) == 5 else False
                books.append(Book(title, author, pages, book_id, borrowed))
            except ValueError as error:
                print(f"Skipping row {line_number}: {error}")
    return books


def find_book(books):
    book_id = input("Enter book ID: ").strip()
    for book in books:
        if book.ID.lower() == book_id.lower():
            return book
    print("Book not found.")
    return None


def main():
    try:
        books = load_books()
    except (OSError, UnicodeError) as error:
        print(f"Could not read {BOOKS_FILE.name}: {error}")
        return
    if not books:
        print("No valid books were found.")
        return

    while True:
        print("\n1. View all books  2. View a book  3. Borrow "
              "4. Return  5. Quit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            for book in books:
                book.display()
        elif choice in ("2", "3", "4"):
            book = find_book(books)
            if book is None:
                continue
            if choice == "2":
                book.display()
            elif choice == "3":
                if book.borrowed:
                    print("This book is already borrowed.")
                else:
                    book.borrowed = True
                    print("Book borrowed successfully.")
            else:
                if not book.borrowed:
                    print("This book is not currently borrowed.")
                else:
                    book.borrowed = False
                    print("Book returned successfully.")
        elif choice == "5":
            print("Goodbye!")
            return
        else:
            print("Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
