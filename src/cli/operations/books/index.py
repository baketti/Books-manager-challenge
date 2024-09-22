from services.books.index import get_book_by_bookId, get_books_by_category, get_books_by_title, get_books_by_authorName, post_book, get_all_books, put_book_by_bookId, delete_book_by_bookId
from cli.inputs.books.index import get_POST_book_input_data, get_PUT_book_input_data, get_book_category
from cli.inputs.index import get_validated_input
from cli.console.books.index import print_books_data
from cli.console.index import print_warning
from rich.prompt import IntPrompt
from cli.menu.books.index import search_books_menu
from services.validation.books.index import validate_title
from services.validation.authors.index import validate_author_name

def post_book_from_CLI():
    book_data = get_POST_book_input_data()
    new_book = post_book(book_data)
    if new_book: print_books_data([new_book], title="New book")

def get_all_books_from_CLI():
    books = get_all_books()
    if books: print_books_data(books)
    else: print_warning("No books found.")

def get_book_by_bookId_from_CLI():
    book_id = IntPrompt.ask("Enter the book ID")
    book = get_book_by_bookId(book_id)
    if book: print_books_data([book], title="Book")
    else: print_warning("Book not found.")

def search_books_by_title_from_CLI():
    title = get_validated_input("Enter the title of the book", validate_title)
    books = get_books_by_title(title)
    if books: print_books_data(books)
    else: print_warning("No books found.")

def search_books_by_author_from_CLI():
    author_name = get_validated_input("Enter the author name", validate_author_name)
    books = get_books_by_authorName(author_name)
    if books: print_books_data(books)
    else: print_warning("No books found.")

def search_books_by_category_from_CLI():
    category = get_book_category()
    books = get_books_by_category(category)
    if books: print_books_data(books)
    else: print_warning("No books found.")

def search_books_from_CLI():
    choice = search_books_menu()
    if choice == '1':
        search_books_by_title_from_CLI()
    elif choice == '2':
        search_books_by_author_from_CLI()
    elif choice == '3':
        search_books_by_category_from_CLI()
    elif choice == '4':
        return

def put_book_by_bookId_from_CLI():
    book_id = IntPrompt.ask("Enter the ID of the book to update")
    book = get_book_by_bookId(book_id)
    if not book:
        print_warning("Cannot update it, this book does not exist!\nRepeat the operation and enter an existing ID.")
        return
    updated_data = get_PUT_book_input_data()
    updated_book = put_book_by_bookId(book, updated_data)
    if updated_book: print_books_data([updated_book], title="Updated book")

def delete_book_by_bookId_from_CLI():
    book_id = IntPrompt.ask("Enter the ID of the book to delete")
    book = get_book_by_bookId(book_id)
    if not book:
        print_warning("Cannot delete it, this book does not exist!\nRepeat the operation and enter an existing ID.")
        return
    delete_book_by_bookId(book_id)