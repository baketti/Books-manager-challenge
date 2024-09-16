import logging

def convert_to_number(value,field_name,field_type):
    if not value or value.strip() == '':
        return None 
    try:
        return field_type(value)
    except ValueError:
        raise ValueError(f"{field_name} must be a number")

def convert_to_dict_list(elements):
    return [element.to_dict() for element in elements]

def disable_sqlalchemy_logging():
    logging.basicConfig()
    logging.getLogger('sqlalchemy').setLevel(logging.ERROR)
    logging.disable(logging.WARNING)
    logging.disable(logging.INFO)
