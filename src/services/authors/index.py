from db.models.Author.index import Author
from cli.console.index import print_success, print_error, print_warning
from db.models.DbConnection.index import DbConnection
from utils.index import is_updated

def post_author(author_data):
    conn = DbConnection.get_connection()
    author = Author(
        name=author_data["name"],
        birth_date=author_data["birth_date"],
        email=author_data["email"]
    )
    try:
        conn.add(author)
        conn.commit()
        print_success("Author created successfully!")
        return author
    except Exception as e:
        conn.roll
        print_error(f"An error occurred during author creation: {e}")

def get_or_create_author(author_name):
    try:
        author = get_author_by_authorName(author_name)
        conn = DbConnection.get_connection()
        if not author:
            return post_author({
                "name": author_name,
                "birth_date": None,
                "email": None
            })
        return author
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred while getting or creating author: {e}")
        return None

def get_author_by_authorId(author_id):
    conn = DbConnection.get_connection()
    try:
        author = conn.query(Author).filter(Author.id == author_id).first()
        return author
    except Exception as e:
        print_error(f"An error occurred during author retrieval: {e}")
        return None

def get_author_by_authorName(author_name):
    conn = DbConnection.get_connection()
    try:
        author = conn.query(Author).filter(Author.name == author_name).first()
        return author
    except Exception as e:
        print_error(f"An error occurred during author retrieval: {e}")
        return None

def get_author_by_email(email):
    conn = DbConnection.get_connection()
    try:
        author = conn.query(Author).filter(Author.email == email).first()
        return author
    except Exception as e:
        print_error(f"An error occurred while searching author by email: {e}")
        return None 

def get_all_authors():
    conn = DbConnection.get_connection()
    try:
        authors = conn.query(Author).all()
        return authors
    except Exception as e:
        print_error(f"An error occurred during authors retrieval: {e}")
        return None

def put_author_by_authorId(author_id, updated_data):
    if not is_updated(updated_data): 
        return None
    author = get_author_by_authorId(author_id)
    conn = DbConnection.get_connection()
    try:
        for key, value in updated_data.items():
            if not value:
                continue
            setattr(author, key, value)
        conn.commit()
        print_success("Author updated successfully!")
        return author
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during author update: {e}")

def delete_author_by_authorId(author_id):
    try:
        author = get_author_by_authorId(author_id)
        print(author.books)
        conn = DbConnection.get_connection()
        if author.books:
            print_warning("Cannot delete author with associated books")
            return
        conn.delete(author)
        conn.commit()
        print_success("Author deleted successfully!")
    except Exception as e:
        conn.rollback()
        print_error(f"An error occurred during author deletion: {e}")