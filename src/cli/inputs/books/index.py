from cli.inputs.index import get_validated_input
from services.validation.books.index import validate_title, validate_pages, validate_price, validate_publisher
from services.validation.authors.index import validate_author_name
from cli.menu.index import prompt_list_choice

def get_POST_book_input_data():
    title = get_validated_input("Title (required)", validate_title, is_required=True)
    author_name = get_validated_input("Author Name (required)", validate_author_name, is_required=True)
    pages = get_validated_input("Number of pages (optional)", validate_pages)
    price = get_validated_input("Cover price (optional)", validate_price)
    publisher = get_validated_input("Publisher (optional)", validate_publisher)
    category = get_book_category()
    return { 
        "title": title,
        "author_name": author_name,
        "pages": pages,
        "price": price,
        "publisher": publisher,
        "category": category
    }

def get_PUT_book_input_data():
    title = get_validated_input("New title", validate_title)
    pages = get_validated_input("New number of pages", validate_pages)
    price = get_validated_input("New cover price", validate_price)
    publisher = get_validated_input("New publisher", validate_publisher)
    category = get_book_category()
    return {
        "title": title,
        "pages": pages,
        "price": price,
        "publisher": publisher,
        "category": category
    }

def get_book_category():
    message = "Select a book category"
    choices = [
        {"name": "Classic", "value": "Classic"},
        {"name": "Drama", "value": "Drama"},
        {"name": "Fantasy", "value": "Fantasy"},
        {"name": "IT", "value": "IT"},
        {"name": "Thriller", "value": "Thriller"},
        {"name": "Miscellaneous", "value": "Miscellaneous"}
    ] 
    return prompt_list_choice(choices, message)