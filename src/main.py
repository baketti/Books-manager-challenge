from cli.console.index import print_exit_message, print_API_start_app
from db.index import create_session
from cli.index import display_main_CLI_app_menu, display_initial_CLI_menu
from app.main import app
from data.index import import_data_from_csv
from rich.prompt import Confirm

def main():
    try:
        connection = create_session()

        need_to_import_data = Confirm.ask("\nDo you want to import data from csv?", default=False)
        if need_to_import_data:
            import_data_from_csv(connection)

        choice = display_initial_CLI_menu()   
        if choice == "1":
            # CLI app
            display_main_CLI_app_menu(connection)
        else:
            # API app
            print_API_start_app()
            app.run()
    except KeyboardInterrupt:
        print_exit_message()
        exit(0)  
       
if __name__ == '__main__':
    main()