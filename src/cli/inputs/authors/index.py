from services.validation.authors.index import validate_author_name, validate_author_birth_date, validate_author_email
from cli.inputs.index import get_validated_input

def get_POST_author_input_data():
    name = get_validated_input("Name (required)", validate_author_name, is_required=True)
    birth_date = get_validated_input("Birth date (YYYY/MM/DD) (optional)", validate_author_birth_date)
    email = get_validated_input("Email (optional)", validate_author_email)
    return {
        "name": name,
        "birth_date": birth_date,
        "email": email
    }

def get_PUT_author_input_data():
    name = get_validated_input("New name", validate_author_name)
    birth_date = get_validated_input("New birth date (YYYY/MM/DD)", validate_author_birth_date)
    email = get_validated_input("New email", validate_author_email)
    return {
        "name": name,
        "birth_date": birth_date,
        "email": email
    }