from rich.console import Console
from rich.theme import Theme
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

theme = Theme({
    "success": "bold green", 
    "error": "bold red", 
    "warning": "yellow"
})

console = Console(theme=theme)

def print_success(message):
    console.print(f"\n✅ {message}", style="success")

def print_error(message):
    console.print(f"\n❌ {message}\n", style="error")

def print_warning(message):
    console.print(f"\n⚠️  {message}\n", style="warning")

def print_title(title):
    _title = " ".join(title)
    title_text = Text(_title, justify="center")
    title_panel = Panel(title_text, expand=True, style="bold magenta", border_style="bright_blue")
    console.print(title_panel)

def print_table(data,columns,title):
    table = Table(title=title, header_style="bold magenta")
    for column in columns:
        table.add_column(column)
    for obj in data:
        row = []
        for value in obj.values():
            row.append(str(value)) 
        table.add_row(*row)
    table_panel = Panel(table, expand=False, border_style="bright_blue")
    console.print(table_panel)

def print_exit_message():
    exit_text = Text("Thank you for using the Library Management System!", justify="center")
    exit_panel = Panel(exit_text, expand=True, style="bold magenta", border_style="bright_blue")
    print("\n")
    console.print(exit_panel)

def print_API_start_app():
    print_title("WELCOME TO THE LIBRARY MANAGEMENT API")
    print("You can test the API with Postman or any tool of your choice.")
    print("\nLocal URL: http://127.0.0.1:5000\n")