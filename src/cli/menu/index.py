from cli.console.index import print_title

def main_menu():
    print_title("WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")
    print("1. Book Management")
    print("2. Author Management")
    print("3. Exit")
    return input("Select an option: ")