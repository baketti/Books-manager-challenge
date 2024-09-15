def get_validated_input(prompt: str, validation_func, is_required: bool=False):
    while True:
        value = input(prompt)
        if not value and not is_required:
            return None
        try:
            _value = validation_func(value)
            return _value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again!")