from cli.console.index import print_title
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def main_menu():
    print_title("WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")
    print_main_menu()
    return Prompt.ask("Select an option", choices=["1", "2", "3"])

def print_main_menu():
    console = Console()
    menu_text = Text()
    menu_text.append("1. ",style="magenta")
    menu_text.append("Books\n")
    menu_text.append("2. ",style="magenta")
    menu_text.append("Authors\n")
    menu_text.append("3. ",style="magenta")
    menu_text.append("Exit", style="bold red")
    menu_panel = Panel.fit(menu_text, style="bold", border_style="bright_blue")
    console.print(menu_panel)