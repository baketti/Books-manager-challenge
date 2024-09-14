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