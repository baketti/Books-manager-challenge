from cli.console.index import print_exit_message
from db.index import create_session
from cli.index import display_CLI_menu

def main():
    try:
        connection = create_session()
        display_CLI_menu(connection)  
    except KeyboardInterrupt:
        print_exit_message()
        exit(0)  
       
if __name__ == '__main__':
    main()