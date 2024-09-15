from services.books.index import get_book_by_bookId, post_book, get_all_books, put_book_by_bookId, delete_book_by_bookId
from services.validation.index import get_validated_input
from services.validation.books.index import validate_title, validate_pages, validate_price
from services.validation.authors.index import validate_author_name

def post_book_from_CLI(connection):
    title = get_validated_input("Title: ", validate_title, is_required=True)
    author_name = get_validated_input("Author Name: ", validate_author_name, is_required=True)
    pages = get_validated_input("Number of pages (optional): ", validate_pages)
    price = get_validated_input("Cover price (optional): ", validate_price)
    publisher = input("Publisher (optional): ")
    book_data = { 
        "title": title,
        "author_name": author_name,
        "pages": pages,
        "price": price,
        "publisher": publisher
    }
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
        title = get_validated_input("New title: ", validate_title)
        author_name = get_validated_input("New author: ", validate_author_name)
        pages = get_validated_input("New number of pages (optional): ", validate_pages)
        price = get_validated_input("New cover price (optional): ", validate_price)
        publisher = input("New publisher (optional): ")
        updated_data = {
            "title": title,
            "author_name": author_name,
            "pages": pages,
            "price": price,
            "publisher": publisher
        }
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