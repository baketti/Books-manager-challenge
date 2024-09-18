from flask import Flask
from app.books.index import books

app = Flask(__name__)
app.register_blueprint(books)