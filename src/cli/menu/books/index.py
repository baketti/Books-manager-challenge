from cli.console.index import print_title
from rich.prompt import Prompt

def books_menu():
    print_title("BOOK MANAGEMENT")
    print("1. Add a book")
    print("2. View all books")
    print("3. View a specific book")
    print("4. Update a book")
    print("5. Delete a book")
    print("6. Return to main menu")
    return Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6"])