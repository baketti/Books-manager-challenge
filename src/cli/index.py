from cli.menu.index import main_menu
from cli.operations.index import books_operations, authors_operations

def display_CLI_menu(connection):
    while True:
        choice = main_menu()
        if choice == '1':
            books_operations(connection)
        elif choice == '2':
            authors_operations(connection)
        elif choice == '3':
            print("Exiting the program.")
            connection.close()
            break
        else:
            print("Invalid choice, please try again.")