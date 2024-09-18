from flask import Flask, request, jsonify
from services.books.index import get_all_books, get_books_by_authorName
from db.models.DbConnection.index import DbConnection
from http import HTTPStatus

db_connection = DbConnection.get_connection()
app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    books = None
    try:
        query_params= request.query_string.decode()
        if not query_params: 
            books = get_all_books(db_connection)
            return (
                jsonify([book.to_dict() for book in books]),
                HTTPStatus.OK)
        else:
            author_name = get_authorName_query_param()
            books = get_books_by_authorName(db_connection, author_name)
            if not books:
                return (
                    jsonify({
                        "message": "No books found"
                    }), 
                    HTTPStatus.NOT_FOUND)
        return (
            jsonify([book.to_dict() for book in books]),
            HTTPStatus.OK)
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during books retrieval: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)

def get_authorName_query_param():
    author_name = request.args.get('authorName')
    sanitized_author_name = ' '.join(author_name.split())
    return sanitized_author_name

if __name__ == "__main__":
    app.run()