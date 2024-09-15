from services.authors.index import delete_author_by_authorId, get_all_authors, get_author_by_authorId, post_author, put_author_by_authorId
from cli.inputs.authors.index import get_POST_author_input_data, get_PUT_author_input_data

def post_author_from_CLI(connection):
    author_data = get_POST_author_input_data()
    post_author(connection, author_data)

def get_all_authors_from_CLI(connection):
    print("List of all authors:")
    authors = get_all_authors(connection)
    if authors:
        for author in authors:
            print(author)
    else:
        print("No authors found.")

def get_author_by_authorId_from_CLI(connection):
    try:
        author_id = int(input("Enter the author ID: "))
        author = get_author_by_authorId(connection, author_id)
        if author:
            print(author)
        else:
            print("Author not found.")
    except ValueError:
        print("Invalid input, ID must be a number.")

def put_author_by_authorId_from_CLI(connection):
    try:
        author_id = int(input("Enter the ID of the author to update: "))
        author = get_author_by_authorId(connection, author_id)
        if not author:
            print("Cannot update it, this author does not exist!\nRepeat the operation and enter an existing ID.")
            return
        updated_data = get_PUT_author_input_data()
        put_author_by_authorId(connection, author_id, updated_data)
    except ValueError:
        print("Invalid input, ID must be a number.")

def delete_author_by_authorId_from_CLI(connection):
    try:
        author_id = int(input("Enter the ID of the author to delete: "))
        author = get_author_by_authorId(connection, author_id)
        if not author:
            print("Cannot delete it, this author does not exist!\nRepeat the operation and enter an existing ID.")
            return
        delete_author_by_authorId(connection, author_id)
    except ValueError:
        print("Invalid input, ID must be a number.")