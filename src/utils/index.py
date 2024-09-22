def convert_to_number(value,field_name,field_type):
    if not value or not value.strip():
        return None 
    try:
        return field_type(value)
    except ValueError:
        raise ValueError(f"{field_name} must be a number")

def convert_to_dict_list(elements):
    return [element.to_dict() for element in elements]

def is_updated(updated_data):
    return any(updated_data[key] != None for key in updated_data.keys())

def sanitize_string(value):
    if not value: return ''
    return ' '.join(value.split())
