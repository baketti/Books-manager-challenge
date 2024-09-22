from cli.console.index import print_error
from InquirerPy import prompt

def get_validated_input(_prompt: str, validation_func, is_required: bool=False):
    while True:
        question = {"type": "input", "message": _prompt, "name": "input"}
        result = prompt(question)
        value = result["input"]
        if not value and not is_required:
            return None
        try:
            _value = validation_func(value)
            return _value
        except ValueError as e:
            print_error(f"Invalid input: {e}. Please try again!")
