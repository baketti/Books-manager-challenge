import os
import csv
from datetime import datetime
from services.authors.index import post_author
from cli.console.index import print_error, print_success

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
        err_msg = f"Error during csv file reading: {e}"
        print_error(err_msg)
        raise FileNotFoundError(err_msg)
    
def create_authors():
    try:
        authors_data = read_authors_csv()
        for author_data in authors_data:
            post_author(author_data)
        print_success(f"Imported {len(authors_data)} authors from csv!\n")
    except Exception as e:
        print_error(e)
