from flask import Blueprint
from app.middleware.index import validate_post_request_body
from db.models.DbConnection.index import DbConnection
from app.routes.books.handlers.post.index import post_books_handler
from app.routes.books.handlers.put.index import put_book_by_id_handler
from app.routes.books.handlers.get.index import get_book_by_id_handler, get_books_handler
from app.routes.books.handlers.delete.index import delete_book_by_id_handler

db_connection = DbConnection.get_connection()
books = Blueprint('books', __name__)

@books.before_request
def check_request_data():
    return validate_post_request_body()

@books.route('/books', methods=['POST'])
def post_books():
    return post_books_handler(db_connection)

@books.route('/books', methods=['GET'])
def get_books():
    print("Get books")
    return get_books_handler(db_connection)

@books.route('/books/<book_id>', methods=['GET'])
def get_book_by_id(book_id):
    return get_book_by_id_handler(db_connection,book_id)

@books.route('/books/<book_id>', methods=['PUT'])
def put_book_by_id(book_id):
    return put_book_by_id_handler(db_connection, book_id)

@books.route('/books/<book_id>', methods=['DELETE'])
def delete_book_by_id(book_id):
    return delete_book_by_id_handler(db_connection, book_id)