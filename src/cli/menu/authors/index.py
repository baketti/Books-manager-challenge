from cli.console.index import print_title
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def authors_menu():
    print_title("AUTHOR MANAGEMENT")
    print_authors_menu()
    return Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6"])

def print_authors_menu():
    console = Console()   

    menu_text = Text()
    menu_text.append("1. ", style="magenta")
    menu_text.append("Add an author\n")
    menu_text.append("2. ", style="magenta")
    menu_text.append("View all authors\n")
    menu_text.append("3. ", style="magenta")
    menu_text.append("View a specific author\n")
    menu_text.append("4. ", style="magenta")
    menu_text.append("Update an author\n")
    menu_text.append("5. ", style="magenta")
    menu_text.append("Delete an author\n")
    menu_text.append("6. ", style="magenta")
    menu_text.append("Return to main menu", style="bold magenta")

    menu_panel = Panel.fit(menu_text, style="bold", border_style="bright_blue")
    console.print(menu_panel)