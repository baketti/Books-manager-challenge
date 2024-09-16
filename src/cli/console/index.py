from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt, Confirm
from rich.console import Console
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
    console.print(f"\n✅ {message}", style="success\n")

def print_error(message):
    console.print(f"\n❌ {message}", style="error\n")

def print_warning(message):
    console.print(f"\n⚠️  {message}", style="warning\n")

def print_title(title):
    _title = " ".join(title)
    title_text = Text(_title, justify="center")
    title_text.stylize("bold bright_blue", 0, len(title_text))
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