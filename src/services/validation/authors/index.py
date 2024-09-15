from datetime import datetime
from email_validator import validate_email, EmailNotValidError

def validate_author_name(name: str):
    if not name:
        raise ValueError("Author name is required")
    if len(name.strip()) < 3:
        raise ValueError("Author name must be at least 3 characters longs")
    else: return name

def validate_author_birth_date(date: str):
    if not date: return None
    try:
        birth_date = datetime.strptime(date, "%Y/%m/%d")
        return birth_date
    except ValueError:
        raise ValueError("Date format must be YYYY/MM/DD")

def validate_author_email(email: str):
    if not email: return None
    try:
        validated_email = validate_email(email)
        _email = validated_email["email"]
        return _email
    except EmailNotValidError as e:
        raise ValueError(e)       
 