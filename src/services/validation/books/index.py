def validate_title(title: str):
    if not title:
        raise ValueError("title is required")
    elif len(title) > 255:
        raise ValueError("title must be at most 255 characters long")
    return title

def validate_pages(pages: int):
    try:
        if pages < 1:
            raise ValueError("pages must be a at least 1")
        elif pages > 10000:
            raise ValueError("Pages must be at most 10000")
        return pages
    except ValueError as e:
        raise ValueError(e)

def validate_price(price: float):
    try:
        if price < 0:
            raise ValueError("price must be at least 0.01$")
        elif price > 10000.00:
            raise ValueError("Price must be at most 10000.00$")
        return price
    except ValueError as e:
        raise ValueError(e)

def validate_publisher(publisher: str):
    if len(publisher) > 255:
        raise ValueError("Publisher must be at most 255 characters long")
    return publisher