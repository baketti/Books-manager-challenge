from cli.console.index import print_title
from rich.prompt import Prompt, Confirm

def main_menu():
    print_title("WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")
    print("1. Book Management")
    print("2. Author Management")
    print("3. Exit")
    return Prompt.ask("Select an option", choices=["1", "2", "3"])