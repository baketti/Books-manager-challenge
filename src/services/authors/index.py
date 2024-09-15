from db.models.Author.index import Author

def post_author(conn, author_data):
    author = Author(
        name=author_data["name"],
        birth_date=author_data["birth_date"],
        email=author_data["email"]
    )
    print("post author->", author)
    try:
        conn.add(author)
        conn.commit()
        print("Author created successfully!")
        return author
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during author creation: {e}")

def get_or_create_author(conn, author_name):
    print('get_or_create_author->',author_name)
    try:
        author = get_author_by_authorName(conn, author_name)
        if not author:
            return post_author(conn, {
                "name": author_name,
                "birth_date": None,
                "email": None
            })
        return author
    except Exception as e:
        conn.rollback()
        print(f"An error occurred while getting or creating author: {e}")
        return None

def get_author_by_authorId(conn, author_id):
    try:
        author = conn.query(Author).filter(Author.id == author_id).first()
        return author
    except Exception as e:
        print(f"An error occurred during author retrieval: {e}")
        return None

def get_author_by_authorName(conn, author_name):
    try:
        author = conn.query(Author).filter(Author.name == author_name).first()
        return author
    except Exception as e:
        print(f"An error occurred during author retrieval: {e}")
        return None

def get_all_authors(conn):
    try:
        authors = conn.query(Author).all()
        return authors
    except Exception as e:
        print(f"An error occurred during authors retrieval: {e}")
        return None

def put_author_by_authorId(conn, author_id, updated_data):
    author = get_author_by_authorId(conn, author_id)
    print("auhor->",author)
    try:
        for key, value in updated_data.items():
            if not value:
                continue
            setattr(author, key, value)
        conn.commit()
        print("Author updated successfully!")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during author update: {e}")

def delete_author_by_authorId(conn, author_id):
    try:
        author = conn.query(Author).filter(Author.id == author_id).first()
        conn.delete(author)
        conn.commit()
        print("Author deleted successfully!")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during author deletion: {e}")