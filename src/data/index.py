from data.authors.index import create_authors
from data.books.index import create_books

def import_data_from_csv(conn):
    create_authors(conn)
    create_books(conn)