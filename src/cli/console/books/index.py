from cli.console.index import print_table
from utils.index import convert_to_dict_list

def print_books_data(books, title="Books"):
    colums = ["ID", "Title", "Author ID", "Pages", "Price", "Publisher"]
    books_data = convert_to_dict_list(books)
    print_table(books_data, colums, title)