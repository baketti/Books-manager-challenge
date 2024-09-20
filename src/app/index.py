from flask import Flask
from app.routes.books.index import books
from app.routes.authors.index import authors

app = Flask(__name__)
app.register_blueprint(books)
app.register_blueprint(authors)