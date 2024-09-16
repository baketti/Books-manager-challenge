from cli.console.index import print_title
from rich.prompt import Prompt

def authors_menu():
    print_title("AUTHOR MANAGEMENT")
    print("1. Add an author")
    print("2. View all authors")
    print("3. View a specific author")
    print("4. Update an author")
    print("5. Delete an author")
    print("6. Return to main menu")
    return Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6"])