from services.validation.authors.index import validate_author_name, validate_author_birth_date, validate_author_email

def validate_post_author_data(author_data):
    try:
        author_name = validate_author_name(author_data.get('name'))
        birth_date = validate_author_birth_date(author_data.get('birth_date', None))
        email = validate_author_email(author_data.get('email', None))
        return {
            "name": author_name,
            "birth_date": birth_date,
            "email": email
        }
    except ValueError as e:
        raise ValueError(e)
    
def validate_put_author_data(author_to_update, author_data):
    try:
        name = validate_author_name(author_data.get('name', author_to_update["name"]))
        birth_date = validate_author_birth_date(author_data.get('birth_date', author_to_update["birth_date"]))
        email = validate_author_email(author_data.get('email', author_to_update["email"]))
        return {
            "name": name,
            "birth_date": birth_date,
            "email": email
        }
    except ValueError as e:
        raise ValueError(e)