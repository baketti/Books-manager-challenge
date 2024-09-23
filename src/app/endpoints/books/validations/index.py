from services.validation.books.index import validate_title, validate_pages, validate_price, validate_publisher, validate_category
from services.validation.authors.index import validate_author_name

def validate_post_book_data(book_data):
    try:
        title = validate_title(book_data.get('title'))
        author_name = validate_author_name(book_data.get('author_name'))
        pages = validate_pages(book_data.get('pages', None))  
        price = validate_price(book_data.get('price', None))
        publisher = validate_publisher(book_data.get('publisher', None))
        category = validate_category(book_data.get('category', None))
        return {
            "title": title,
            "author_name": author_name,
            "pages": pages,
            "price": price,
            "publisher": publisher,
            "category": category
        }
    except ValueError as e:
        raise ValueError(e)
    
def validate_put_book_data(book_to_update, book_data):
    try:
        title = validate_title(book_data.get('title', book_to_update["title"]))
        pages = validate_pages(book_data.get('pages', book_to_update["pages"]))
        price = validate_price(book_data.get('price', book_to_update["price"]))
        publisher = validate_publisher(book_data.get('publisher', book_to_update["publisher"]))
        category = validate_category(book_data.get('category', book_to_update["category"]))
        return {
            "title": title,
            "pages": pages,
            "price": price,
            "publisher": publisher,
            "category": category
        }
    except ValueError as e:
        raise ValueError(e)