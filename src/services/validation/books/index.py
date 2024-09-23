from utils.index import convert_to_number, sanitize_string

def validate_title(_title: str):
    if _title and type(_title) != str:
        raise ValueError("Book title must be a string")
    title = sanitize_string(_title)
    if not title:
        raise ValueError("title is required")
    elif len(title) > 255:
        raise ValueError("title must be at most 255 characters long")
    return title

def validate_pages(pages: str):
    try:
        _pages = convert_to_number(pages,'pages',int)
        if _pages and _pages < 1:
            raise ValueError("pages must be a at least 1")
        elif _pages and _pages > 10000:
            raise ValueError("Pages must be at most 10000")
        return _pages
    except ValueError as e:
        raise ValueError(e)

def validate_price(price: str):
    try:
        _price = convert_to_number(price,'price',float)
        if _price and _price < 0:
            raise ValueError("price must be at least 0.01$")
        elif _price and _price > 10000.00:
            raise ValueError("Price must be at most 10000.00$")
        return _price
    except ValueError as e:
        raise ValueError(e)
    
def validate_publisher(_publisher: str):
    if not _publisher or not _publisher.strip(): return None
    if type(_publisher) != str:
        raise ValueError("Book publisher must be a string")
    publisher = sanitize_string(_publisher)
    if len(publisher) > 255:
        raise ValueError("Publisher must be at most 255 characters long")
    return publisher

def validate_category(category: str):
    if not category or not category.strip(): return None
    categories = ["Classic", "Drama", "Fantasy", "IT", "Thriller", "Miscellaneous"]
    if category not in categories:
        raise ValueError("Category must be one of the following: Classic, Drama, Fantasy, IT, Thriller, Miscellaneous")
    return category