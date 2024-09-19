from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from utils.index import sanitize_string

def validate_author_name(_name: str):
    name = sanitize_string(_name)
    if not name:
        raise ValueError("Author name is required")
    if len(name) < 3:
        raise ValueError("Author name must be at least 3 characters longs")
    elif len(name) > 32:
        raise ValueError("Author name must be at most 32 characters long")
    else: return name

def validate_author_birth_date(date: str):
    try:
        birth_date = datetime.strptime(date, "%Y/%m/%d")
        return birth_date
    except ValueError:
        raise ValueError("Date format must be YYYY/MM/DD")

def validate_author_email(email: str):
    try:
        validated_email = validate_email(email)
        _email = validated_email["email"]
        return _email
    except EmailNotValidError as e:
        raise ValueError(e)       
 