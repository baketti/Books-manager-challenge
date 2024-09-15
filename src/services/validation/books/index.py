from utils.functions.index import convert_to_number
#TODO add all necessary conditions  

def validate_title(title: str):
    if not title:
        raise ValueError("title is required")
    else: return title
    """ if len(title) < 1:
        raise ValueError("Title must be at least 1 character long.") """

def validate_pages(pages: str):
    try:
        _pages = convert_to_number(pages,'pages',int)
        if _pages and _pages < 0:
            raise ValueError("pages must be a positive integer")
        return _pages
    except ValueError as e:
        raise ValueError(e)

def validate_price(price: str):
    try:
        _price = convert_to_number(price,'price',float)
        if _price and _price < 0:
            raise ValueError("price must be a positive number")
        return _price
    except ValueError as e:
        raise ValueError(e)

#TODO add validation for publisher 
def validate_publisher(publisher: str):
    return publisher