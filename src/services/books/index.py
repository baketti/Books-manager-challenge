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