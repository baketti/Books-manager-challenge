import os
import csv
from datetime import datetime
from services.authors.index import post_author
from cli.console.index import print_error

def read_authors_csv():
    try:
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "authors.csv")
        with open(file_path, newline="", encoding="ISO-8859-1") as filecsv:      
            reader = csv.reader(filecsv,delimiter=",")
            data = []
            for row in reader:
                data.append({
                "name": row[0],
                "birth_date": datetime.strptime(row[1], "%Y/%m/%d"),
                "email": row[2]
            })
            return data
    except FileNotFoundError as e:
        print_error(f"Error during csv file reading: {e}")
        return None
    
def create_authors(conn):
    authors_data = read_authors_csv()
    if authors_data:
        for author_data in authors_data:
            post_author(conn, author_data)