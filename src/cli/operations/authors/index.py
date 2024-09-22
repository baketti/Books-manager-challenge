from cli.inputs.index import get_validated_input
from cli.menu.authors.index import print_search_authors_menu
from services.authors.index import delete_author_by_authorId, get_all_authors, get_author_by_authorId, get_author_by_authorName, post_author, put_author_by_authorId
from cli.inputs.authors.index import get_POST_author_input_data, get_PUT_author_input_data
from cli.console.authors.index import print_authors_data
from cli.console.index import print_warning
from rich.prompt import IntPrompt, Confirm
from services.validation.authors.index import validate_author_name

def post_author_from_CLI():
    author_data = get_POST_author_input_data()
    new_author = post_author(author_data)
    if new_author: print_authors_data([new_author], title="New author")

def get_all_authors_from_CLI():
    authors = get_all_authors()
    if authors: print_authors_data(authors)
    else: print_warning("No authors found.")

def get_author_by_authorId_from_CLI():
    author_id = IntPrompt.ask("Enter the author ID")
    author = get_author_by_authorId(author_id)
    if author: print_authors_data([author], title="Author")
    else: print_warning("Author not found.")

def search_author_by_name_from_CLI():
    author_name = get_validated_input("Enter the author name", validate_author_name)
    author = get_author_by_authorName(author_name)
    if author: print_authors_data([author], title="Author found")
    else: print_warning("No authors found.")

def search_author_from_CLI():
    print_search_authors_menu()
    search = Confirm.ask("Do you want to search by author name or not?", default=True)
    if not search: 
        return
    search_author_by_name_from_CLI()

def put_author_by_authorId_from_CLI():
    author_id = IntPrompt.ask("Enter the ID of the author to update")
    author = get_author_by_authorId(author_id)
    if not author:
        print_warning("Cannot update it, this author does not exist!\nRepeat the operation and enter an existing ID.")
        return
    updated_data = get_PUT_author_input_data()
    update_book = put_author_by_authorId(author_id, updated_data)
    if update_book: print_authors_data([update_book], title="Updated author")

def delete_author_by_authorId_from_CLI():
    author_id = IntPrompt.ask("Enter the ID of the author to delete")
    author = get_author_by_authorId(author_id)
    if not author:
        print_warning("Cannot delete it, this author does not exist!\nRepeat the operation and enter an existing ID.")
        return
    delete_author_by_authorId(author_id)