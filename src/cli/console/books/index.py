from cli.console.index import print_table
from utils.functions.index import convert_to_dict_list

def print_books_data(books):
    colums = ["ID", "Title", "Author ID", "Pages", "Price", "Publisher"]
    books_data = convert_to_dict_list(books)
    print_table(colums, books_data, "Books")