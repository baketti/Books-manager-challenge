from rich.prompt import Prompt, IntPrompt, FloatPrompt

def get_validated_input(prompt: str, validation_func, field_type=str, is_required: bool=False):
    while True:
        value = None
        if field_type == int: 
            value = IntPrompt.ask(prompt)
        elif field_type == float: 
            value = FloatPrompt.ask(prompt)
        else: 
            value = Prompt.ask(prompt)

        if not value and not is_required:
            return None
        try:
            _value = validation_func(value)
            return _value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again!")