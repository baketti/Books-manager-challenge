from services.books.index import get_book_by_bookId, post_book, get_all_books, put_book_by_bookId, delete_book_by_bookId
from cli.inputs.books.index import get_POST_book_input_data, get_PUT_book_input_data
from cli.console.books.index import print_books_data
from cli.console.index import print_error, print_warning

def post_book_from_CLI(connection):
    book_data = get_POST_book_input_data()
    new_book = post_book(connection, book_data)
    if new_book: print_books_data([new_book])

def get_all_books_from_CLI(connection):
    books = get_all_books(connection)
    if books: print_books_data(books)
    else: print_warning("No books found.")

def get_book_by_bookId_from_CLI(connection):
    try:
        book_id = int(input("Enter the book ID: "))
        book = get_book_by_bookId(connection, book_id)
        if book: print_books_data([book])
        else: print_warning("Book not found.")
    except ValueError:
        print_error("Invalid input, ID must be a number.")

def put_book_by_bookId_from_CLI(connection):
    try:
        book_id = int(input("Enter the ID of the book to update: "))
        book = get_book_by_bookId(connection, book_id)
        if not book:
            print_warning("Cannot update it, this book does not exist!\nRepeat the operation and enter an existing ID.")
            return
        updated_data = get_PUT_book_input_data()
        updated_book = put_book_by_bookId(connection, book_id, updated_data)
        if updated_book: print_books_data([updated_book])
    except ValueError:
        print_error("Invalid input, ID must be a number.")

def delete_book_by_bookId_from_CLI(connection):
    try:
        book_id = int(input("Enter the ID of the book to delete: "))
        book = get_book_by_bookId(connection, book_id)
        if not book:
            print_warning("Cannot delete it, this book does not exist!\nRepeat the operation and enter an existing ID.")
            return
        delete_book_by_bookId(connection, book_id)
    except ValueError:
        print_error("Invalid input, ID must be a number.")