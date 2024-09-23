from cli.console.index import print_error
from data.authors.index import create_authors
from data.books.index import create_books

def import_data_from_csv():
    try:
        create_authors()
        create_books()
    except Exception as e:
        print_error(e)
    