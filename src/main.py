from cli.console.index import print_exit_message, print_API_start_app
from cli.index import display_main_CLI_app_menu, display_initial_CLI_menu
from app.index import create_app
from data.index import import_data_from_csv
from rich.prompt import Confirm
from db.models.DbConnection.index import DbConnection 

def main():
    try:
        DbConnection()
        need_to_import_data = Confirm.ask("\nDo you want to import data from csv?", default=True)
        if need_to_import_data:
            import_data_from_csv()
        choice = display_initial_CLI_menu()   
        if choice == "1":
            # CLI app
            display_main_CLI_app_menu()
        else:
            # API app
            print_API_start_app()
            app = create_app()
            app.run()
    except KeyboardInterrupt:
        print_exit_message()
        exit(0)  
    except Exception as e:
        print(f"An error occurred: {e}")
        print_exit_message()
        exit(1)
       
if __name__ == '__main__':
    main()