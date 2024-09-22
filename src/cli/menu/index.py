from cli.console.index import print_title
from InquirerPy import prompt

qa_style = {
    "questionmark": "magenta bold",
    "pointer": "#61afef bold",
    "answer": "magenta",
}

def initial_cli_menu():
    message = "Do you want to use CLI app or API?"
    choices = [
        {"name": "CLI", "value": "1"},
        {"name": "API", "value": "2"}
    ]
    return prompt_list_choice(choices, message)

def main_cli_app_menu():
    print_title("WELCOME TO THE LIBRARY MANAGEMENT CLI SYSTEM") 
    message = "Go to books or authors menu"
    choices = [
        {"name": "Books", "value": "1"}, 
        {"name": "Authors", "value": "2"}, 
        {"name": "Exit", "value": "3"}
    ]
    return prompt_list_choice(choices, message)

def prompt_list_choice(choices, message):
    req = {
            "type": "list", 
            "message": message, 
            "choices": choices, 
            "name": "choice"
        }
    res = prompt(req,style=qa_style)
    return res["choice"]
