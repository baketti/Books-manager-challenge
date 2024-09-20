from datetime import datetime, date
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

def validate_author_birth_date(birth_date: str|date):
    if not birth_date:
        #works only for apis
        return None
    elif isinstance(birth_date, date):
        #works only for apis
        return birth_date

    try:
        birth_date = datetime.strptime(birth_date, "%Y/%m/%d")
        return birth_date
    except ValueError:
        raise ValueError("date format must be YYYY/MM/DD")
    except TypeError:
        raise ValueError("date must be a string")

def validate_author_email(email: str):
    if not email:
        #works only for apis
        return None
    elif type(email) != str:
        #works only for apis
        raise ValueError("email must be a string")
    try:
        validated_email = validate_email(email)
        _email = validated_email["email"]
        return _email
    except ValueError as e:
        raise ValueError(e)
    except EmailNotValidError as e:
        raise ValueError(f"invalid email ({e})")       
 