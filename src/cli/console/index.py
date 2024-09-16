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
    table = Table(title=title)
    for column in columns:
        table.add_column(column)
    for obj in data:
        row = []
        for value in obj.values():
            row.append(str(value)) 
        table.add_row(*row)
    console.print(table)

def print_exit_message():
    exit_text = Text("Thank you for using the Library Management System!", justify="center")
    exit_panel = Panel(exit_text, expand=True, style="bold magenta", border_style="bright_blue")
    console.print(exit_panel)