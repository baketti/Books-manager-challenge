from cli.console.index import print_table
from utils.index import convert_to_dict_list

def print_authors_data(authors, title="Authors"):
    colums = ["ID", "Name", "Birth date", "Email"]
    authors_data = convert_to_dict_list(authors)
    print_table(authors_data, colums, title)