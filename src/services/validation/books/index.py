from utils.functions.index import convert_to_number

def validate_title(title: str):
    if not title:
        raise ValueError("title is required")
    elif len(title) > 255:
        raise ValueError("title must be at most 255 characters long")
    return title

def validate_pages(pages: str):
    try:
        _pages = convert_to_number(pages,'pages',int)
        if _pages < 1:
            raise ValueError("pages must be a at least 1")
        elif _pages > 10000:
            raise ValueError("Pages must be at most 10000")
        return _pages
    except ValueError as e:
        raise ValueError(e)

def validate_price(price: str):
    try:
        _price = convert_to_number(price,'price',float)
        if _price < 0:
            raise ValueError("price must be at least 0.01$")
        elif _price > 10000.00:
            raise ValueError("Price must be at most 10000.00$")
        return _price
    except ValueError as e:
        raise ValueError(e)
    
def validate_publisher(publisher: str):
    if len(publisher) > 255:
        raise ValueError("Publisher must be at most 255 characters long")
    return publisher