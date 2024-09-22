from flask import Flask
from app.endpoints.books.index import books
from app.endpoints.authors.index import authors

app = Flask(__name__)
app.register_blueprint(books)
app.register_blueprint(authors)