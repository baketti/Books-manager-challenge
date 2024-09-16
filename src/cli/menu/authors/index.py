from cli.console.index import print_title

def authors_menu():
    print_title("AUTHOR MANAGEMENT")
    print("1. Add an author")
    print("2. View all authors")
    print("3. View a specific author")
    print("4. Update an author")
    print("5. Delete an author")
    print("6. Return to main menu")
    return input("Select an option: ")