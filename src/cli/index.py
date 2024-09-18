from cli.menu.index import initial_cli_menu, main_cli_app_menu
from cli.operations.index import books_operations, authors_operations
from rich.prompt import Confirm
from cli.console.index import print_exit_message

def display_initial_CLI_menu():
    return initial_cli_menu()

def display_main_CLI_app_menu(connection):
    while True:
        choice = main_cli_app_menu()
        if choice == '1':
            books_operations(connection)
        elif choice == '2':
            authors_operations(connection)
        elif choice == '3':
            exit = Confirm.ask("Are you sure you want to exit the program?", default="y")
            if exit:
                print_exit_message()
                connection.close()
                break
