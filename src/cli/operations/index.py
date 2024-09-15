from cli.menu.authors.index import authors_menu
from cli.operations.authors.index import post_author_from_CLI,get_all_authors_from_CLI,get_author_by_authorId_from_CLI,put_author_by_authorId_from_CLI,delete_author_by_authorId_from_CLI

def authors_operations(connection):
    while True:
        choice = authors_menu()
        if choice == '1':
            post_author_from_CLI(connection)
        elif choice == '2':
            get_all_authors_from_CLI(connection)
        elif choice == '3':
            get_author_by_authorId_from_CLI(connection)
        elif choice == '4':
            put_author_by_authorId_from_CLI(connection)
        elif choice == '5':
            delete_author_by_authorId_from_CLI(connection)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")