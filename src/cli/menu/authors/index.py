from cli.console.index import print_title
from cli.menu.index import prompt_list_choice

def authors_menu():
    print_title("AUTHORS MANAGEMENT")
    message = "Select an option"
    choices = [
        {"name": "Add an author", "value": "1"},
        {"name": "View all authors", "value": "2"},
        {"name": "View a specific author", "value": "3"},
        {"name": "Search author", "value": "4"},
        {"name": "Update an author", "value": "5"},
        {"name": "Delete an author", "value": "6"},
        {"name": "Return to main menu", "value": "7"},
    ]
    return prompt_list_choice(choices, message)