from services.books.index import get_all_books
from db.models.DbConnection.index import DbConnection
from flask import Blueprint, jsonify, request

db_connection = DbConnection().get_connection()
books_bp = Blueprint('books', __name__)

# TODO
@books_bp.route('/books', methods=['GET'])
def get_books():
    return (
        jsonify({"message": "Not implemented yet"}), 
        501
    )