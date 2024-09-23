from flask import Flask
from app.endpoints.books.index import books
from app.endpoints.authors.index import authors
from cli.console.index import print_exit_message

def create_app():
    try:
        app = Flask(__name__)
        app.register_blueprint(books)
        app.register_blueprint(authors)
        return app
    except KeyboardInterrupt:
        print_exit_message()
        exit(0)