from cli.console.index import print_title
from cli.menu.index import prompt_list_choice

def books_menu():
    print_title("BOOKS MANAGEMENT")
    message = "Select an option"
    choices = [
        {"name": "Add a book", "value": "1"}, 
        {"name": "View all books", "value": "2"}, 
        {"name": "View a specific book", "value": "3"}, 
        {"name": "Search books", "value": "4"}, 
        {"name": "Update a book", "value": "5"}, 
        {"name": "Delete a book", "value": "6"}, 
        {"name": "Return to main menu", "value": "7"},
    ]
    return prompt_list_choice(choices, message)

def search_books_menu():
    message = "Do you want to search by title, author name or category?"
    choices = [
        {"name": "Title", "value": "1"},
        {"name": "Author name", "value": "2"},
        {"name": "Category", "value": "3"},
        {"name": "Return to books menu", "value": "4"}
    ]
    return prompt_list_choice(choices, message)