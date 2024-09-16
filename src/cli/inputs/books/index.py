from cli.inputs.index import get_validated_input
from services.validation.books.index import validate_title, validate_pages, validate_price, validate_publisher
from services.validation.authors.index import validate_author_name

def get_POST_book_input_data():
    title = get_validated_input("Title", validate_title, is_required=True)
    author_name = get_validated_input("Author Name", validate_author_name, is_required=True)
    pages = get_validated_input("Number of pages (optional)", validate_pages, field_type=int)
    price = get_validated_input("Cover price (optional)", validate_price, field_type=float)
    publisher = get_validated_input("Publisher (optional)", validate_publisher)
    return { 
        "title": title,
        "author_name": author_name,
        "pages": pages,
        "price": price,
        "publisher": publisher
    }

def get_PUT_book_input_data():
    title = get_validated_input("New title", validate_title)
    author_name = get_validated_input("New author", validate_author_name)
    pages = get_validated_input("New number of pages (optional)", validate_pages)
    price = get_validated_input("New cover price (optional)", validate_price)
    publisher = get_validated_input("New publisher (optional)", validate_publisher)
    return {
        "title": title,
        "author_name": author_name,
        "pages": pages,
        "price": price,
        "publisher": publisher
    }