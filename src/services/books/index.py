from db.models.Book.index import Book
from db.models.DbConnection.index import DbConnection
from services.authors.index import get_author_by_authorName, get_or_create_author
from cli.console.index import print_success,print_error
from utils.index import is_updated

def post_book(book_data):
    conn = DbConnection.get_connection()
    author = get_or_create_author(book_data['author_name'])
    print(author.to_dict())
    book = Book(
        title=book_data["title"],
        author_id=author.id,
        pages=book_data["pages"],
        price=book_data["price"],
        publisher=book_data["publisher"],
        category=book_data["category"]
    )
    try:
        conn.add(book)
        conn.commit()
        print_success("Book created successfully!")
        return book
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book creation: {e}")
        raise Exception(e)

def get_book_by_bookId(book_id):
    conn = DbConnection.get_connection()
    try:
        book = conn.query(Book).filter(Book.id == book_id).first()
        return book
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book retrieval: {e}")
        return None

def get_books_by_authorName(author_name):
    conn = DbConnection.get_connection()
    try:
        author = get_author_by_authorName(author_name)
        if not author:
            return None
        return author.books
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during books retrieval: {e}")
        return None

def get_books_by_title(title):
    conn = DbConnection.get_connection()
    try:
        books = conn.query(Book).filter(Book.title.contains(title)).all()
        return books
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book retrieval: {e}")
        return None
    
def get_all_books():
    conn = DbConnection.get_connection()
    try:
        books = conn.query(Book).all()
        return books
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book list retrieval: {e}")
        return None

def put_book_by_bookId(book, updated_data):
    if not is_updated(updated_data): 
        return None        
    conn = DbConnection.get_connection()    
    try:
        for key, value in updated_data.items():
            if not value:
                continue
            setattr(book, key, value)
        conn.commit()
        print_success("Book updated successfully!")
        return book
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book update: {e}")

def delete_book_by_bookId(book_id):
    conn = DbConnection.get_connection()
    try:
        book = conn.query(Book).filter(Book.id == book_id).first()
        conn.delete(book)
        conn.commit()
        print_success("Book deleted successfully!")
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during book deletion: {e}")