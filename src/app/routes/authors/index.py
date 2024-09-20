from flask import Blueprint
from db.models.DbConnection.index import DbConnection
from app.routes.authors.validations.index import validate_post_author_data
from app.routes.authors.handlers.post.index import post_authors_handler
from app.routes.authors.handlers.get.index import get_authors_handler, get_author_by_id_handler
from app.routes.authors.handlers.put.index import put_author_by_id_handler
from app.routes.authors.handlers.delete.index import delete_author_by_id_handler
from app.middleware.index import validate_post_request_body

db_connection = DbConnection.get_connection()
authors = Blueprint('authors', __name__)

@authors.before_request
def check_request_data():
    return validate_post_request_body()

@authors.route('/authors', methods=['POST'])
def post_author():
    return post_authors_handler(db_connection)

@authors.route('/authors', methods=['GET'])
def get_authors():
    return get_authors_handler(db_connection)

@authors.route('/authors/<author_id>', methods=['GET'])
def get_author_by_id(author_id):
    return get_author_by_id_handler(db_connection, author_id)

@authors.route('/authors/<author_id>', methods=['PUT'])
def put_author_by_id(author_id):
    return put_author_by_id_handler(db_connection, author_id)

@authors.route('/authors/<author_id>', methods=['DELETE'])
def delete_author_by_id(author_id):
    return delete_author_by_id_handler(db_connection, author_id)