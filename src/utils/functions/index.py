def convert_to_number(value,field_name,field_type):
    if not value or value.strip() == '':
        return None 
    try:
        return field_type(value)
    except ValueError:
        raise ValueError(f"{field_name} must be a number")