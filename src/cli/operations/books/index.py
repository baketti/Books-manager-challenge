from services.books.index import get_book_by_bookId, post_book, get_all_books, put_book_by_bookId, delete_book_by_bookId
from cli.inputs.books.index import get_POST_book_input_data, get_PUT_book_input_data

def post_book_from_CLI(connection):
    book_data = get_POST_book_input_data()
    post_book(connection, book_data)

def get_all_books_from_CLI(connection):
    print("List of all books:")
    books = get_all_books(connection)
    if books:
        for book in books:
            print(book)
    else:
        print("No books found.")

def get_book_by_bookId_from_CLI(connection):
    try:
        book_id = int(input("Enter the book ID: "))
        book = get_book_by_bookId(connection, book_id)
        if book:
            print(book)
        else:
            print("Book not found.")
    except ValueError:
        print("Invalid input, ID must be a number.")

def put_book_by_bookId_from_CLI(connection):
    try:
        book_id = int(input("Enter the ID of the book to update: "))
        book = get_book_by_bookId(connection, book_id)
        if not book:
            print("Cannot update it, this book does not exist!\nRepeat the operation and enter an existing ID.")
            return
        updated_data = get_PUT_book_input_data()
        put_book_by_bookId(connection, book_id, updated_data)
    except ValueError:
        print("Invalid input, ID must be a number.")

def delete_book_by_bookId_from_CLI(connection):
    try:
        book_id = int(input("Enter the ID of the book to delete: "))
        book = get_book_by_bookId(connection, book_id)
        if not book:
            print("Cannot delete it, this book does not exist!\nRepeat the operation and enter an existing ID.")
            return
        delete_book_by_bookId(connection, book_id)
    except ValueError:
        print("Invalid input, ID must be a number.")