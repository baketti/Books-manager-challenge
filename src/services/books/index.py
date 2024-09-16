from db.models.Book.index import Book
from services.authors.index import get_or_create_author
from cli.console.index import print_success,print_error
from utils.functions.index import is_updated

def post_book(conn, book_data):
    author = get_or_create_author(conn, book_data['author_name'])
    book = Book(
        title=book_data["title"],
        author_id=author.id,
        pages=book_data["pages"],
        price=book_data["price"],
        publisher=book_data["publisher"]
    )
    try:
        conn.add(book)
        conn.commit()
        print_success("Book created successfully!")
        return book
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book creation: {e}")

def get_all_books(conn):
    try:
        books = conn.query(Book).all()
        return books
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book list retrieval: {e}")
        return None

def get_book_by_bookId(conn, book_id):
    try:
        book = conn.query(Book).filter(Book.id == book_id).first()
        return book
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book retrieval: {e}")
        return None

def put_book_by_bookId(conn, book_id, updated_data):
    if not is_updated(updated_data): 
        return None
    book = get_book_by_bookId(conn, book_id)
    author_name = updated_data["author_name"]
    if author_name:
        author = get_or_create_author(conn, author_name)
        setattr(book, "author_id", author.id)
    try:
        for key, value in updated_data.items():
            if key == "author_name" or not value:
                continue
            setattr(book, key, value)
        conn.commit()
        print_success("Book updated successfully!")
        return book
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book update: {e}")

def delete_book_by_bookId(conn, book_id):
    try:
        book = conn.query(Book).filter(Book.id == book_id).first()
        conn.delete(book)
        conn.commit()
        print_success("Book deleted successfully!")
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book deletion: {e}")