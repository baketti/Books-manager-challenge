import os
import csv
from services.books.index import post_book      
from cli.console.index import print_error, print_success

def read_books_csv():
    try:
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "books.csv")
        with open(file_path, newline="", encoding="ISO-8859-1") as filecsv:
            reader = csv.reader(filecsv,delimiter=",")
            data = []
            for row in reader:
                data.append({
                    "title": row[0],
                    "author_name": row[1],
                    "pages": row[2],
                    "price": row[3],
                    "publisher": row[4],
                    "category": row[5]
                })
            return data
    except FileNotFoundError as e:
        err_msg = f"Error during books csv file reading: {e}"
        print_error(err_msg)
        raise FileNotFoundError(err_msg)

def create_books():
    try:
        books_data = read_books_csv()
        for book_data in books_data:
            post_book(book_data)
        print_success(f"Imported {len(books_data)} books from csv!\n")
    except Exception as e:
        print_error(e)
    
