def get_validated_input(prompt: str, validation_func, type=None) -> str|type:
    while True:
        value = input(prompt)
        try:
            _value = validation_func(value)
            if(type and _value): 
                return type(_value)
            else:
                return _value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again!")