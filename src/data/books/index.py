import os
import csv
from services.books.index import post_book      
from cli.console.index import print_error

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
                    "publisher": row[4]
                })
            return data
    except FileNotFoundError as e:
        print_error(f"Error during books csv file reading: {e}")
        return None

def create_books(conn):
    books_data = read_books_csv()
    if books_data:
        for book_data in books_data:
            post_book(conn, book_data)