from cli.console.index import print_title
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def books_menu():
    print_title("BOOK MANAGEMENT")
    print_books_menu()
    return Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6"])

def print_books_menu():
    console = Console()
    menu_text = Text()
    menu_text.append("1. ",style="magenta")
    menu_text.append("Add a book\n")
    menu_text.append("2. ",style="magenta")
    menu_text.append("View all books\n")
    menu_text.append("3. ",style="magenta")
    menu_text.append("View a specific book\n")
    menu_text.append("4. ",style="magenta")
    menu_text.append("Update a book\n")
    menu_text.append("5. ",style="magenta")
    menu_text.append("Delete a book\n")
    menu_text.append("6. ",style="magenta")
    menu_text.append("Return to main menu", style="bold magenta")
    menu_panel = Panel.fit(menu_text, style="bold", border_style="bright_blue")
    console.print(menu_panel)