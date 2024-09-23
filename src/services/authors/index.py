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
        if str(e).startswith("(sqlite3.IntegrityError) UNIQUE constraint failed: authors.name"):
            print_error(f"Author with name '{author_data['name']}' already exists!")
            raise Exception(f"Author with name '{author_data['name']}' already exists!")
        conn.rollback()
        print_error(f"An error occurred during author creation: {e}")
        raise Exception(e)

def get_or_create_author(author_name):
    try:
        author = get_authors_by_authorName(author_name)
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
        raise Exception(e)

def get_author_by_authorId(author_id):
    conn = DbConnection.get_connection()
    try:
        author = conn.query(Author).filter(Author.id == author_id).first()
        if not author: return None
        return author
    except Exception as e:
        print_error(f"An error occurred during author retrieval: {e}")
        raise Exception(e)

def get_authors_by_authorName(author_name, is_search=False):
    conn = DbConnection.get_connection()
    try:
        if not is_search:
            author = conn.query(Author).filter(Author.name == author_name).first()
            return author
        authors = conn.query(Author).filter(Author.name.contains(author_name)).all()
        if not authors: return None
        return authors
    except Exception as e:
        print_error(f"An error occurred during author retrieval: {e}")
        raise Exception(e)

def get_authors_by_email(email, is_search=False):
    conn = DbConnection.get_connection()
    try:
        if not is_search:
            author = conn.query(Author).filter(Author.email == email).first()
            return author
        authors = conn.query(Author).filter(Author.email.contains(email)).all()
        if not authors: return None
        return authors
    except Exception as e:
        print_error(f"An error occurred while searching author by email: {e}")
        raise Exception(e)

def get_all_authors(limit=None):
    conn = DbConnection.get_connection()
    try:
        authors = conn.query(Author).limit(limit).all()
        if not authors: return None
        return authors
    except Exception as e:
        print_error(f"An error occurred during authors retrieval: {e}")
        raise Exception(e)

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
        raise Exception(e)

def delete_author_by_authorId(author_id):
    try:
        author = get_author_by_authorId(author_id)
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
        raise Exception(e)