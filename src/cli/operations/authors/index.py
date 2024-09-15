from services.authors.index import delete_author_by_authorId, get_all_authors, get_author_by_authorId, post_author, put_author_by_authorId
from services.validation.authors.index import validate_author_name, validate_author_birth_date, validate_author_email
from services.validation.index import get_validated_input

def post_author_from_CLI(connection):
    name = get_validated_input("Name: ", validate_author_name)
    birth_date = get_validated_input("Birth date (YYYY/MM/DD): ", validate_author_birth_date)
    email = get_validated_input("Email: ", validate_author_email)
    author_data = {
        "name": name,
        "birth_date": birth_date,
        "email": email
    }
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
    author_id = int(input("Enter the author ID: "))
    author = get_author_by_authorId(connection, author_id)
    if author:
        print(author)
    else:
        print("Author not found.")

def put_author_by_authorId_from_CLI(connection):
    author_id = int(input("Enter the ID of the author to update: "))
    name = get_validated_input("New name: ", validate_author_name)
    birth_date = get_validated_input("New birth date (YYYY/MM/DD): ", validate_author_birth_date)
    email = get_validated_input("New email: ", validate_author_email)
    updated_data = {
        "name": name,
        "birth_date": birth_date,
        "email": email
    }
    put_author_by_authorId(connection, author_id, updated_data)

def delete_author_by_authorId_from_CLI(connection):
    author_id = int(input("Enter the ID of the author to delete: "))
    delete_author_by_authorId(connection, author_id)