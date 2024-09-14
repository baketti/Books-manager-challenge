from db.models.Book.index import Book
from services.authors.index import get_or_create_author

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
        print("Book added successfully!")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during book creation: {e}")

def get_all_books(conn):
    try:
        books = conn.query(Book).all()
        return books
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during book list retrieval: {e}")
        return None

def get_book_by_bookId(conn, book_id):
    try:
        book = conn.query(Book).filter(Book.id == book_id).first()
        return book
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during book retrieval: {e}")
        return None

def put_book_by_bookId(conn, book_id, updated_data):
    book = get_book_by_bookId(conn, book_id)#retrieve book to update to set its values if they are not provided
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
        print("Book updated successfully!")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during book update: {e}")

def delete_book_by_bookId(conn, book_id):
    try:
        book = conn.query(Book).filter(Book.id == book_id).first()
        conn.delete(book)
        conn.commit()
        print("Book deleted successfully!")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during book deletion: {e}")