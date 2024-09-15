from db.index import create_session
from cli.index import display_CLI_menu

def main():
    connection = create_session()
    display_CLI_menu(connection)    
       
if __name__ == '__main__':
    main()