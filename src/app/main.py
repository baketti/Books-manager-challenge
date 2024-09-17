from flask import Flask, request, jsonify
from services.books.index import get_all_books, get_books_by_authorName
from db.models.DbConnection.index import DbConnection
from http import HTTPStatus

db_connection = DbConnection.get_connection()
app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    books = None
    query_params= request.query_string.decode()
    if not query_params: 
        books = get_all_books(db_connection)
    else:
        author_name = get_authorName_query_param(query_params)
        books = get_books_by_authorName(db_connection, author_name)
        if not books:
            return (
                jsonify({
                    "message": "No books found"
                }), 
                HTTPStatus.NOT_FOUND
            )
        
    return (
        jsonify(
            [book.to_dict() for book in books]
        ),
        HTTPStatus.OK
    )

def get_authorName_query_param(query_params):
    params = query_params.split('&')
    query_items = [{param.split('=')[0]: param.split('=')[1]} for param in params]
    print(query_items)
    authorName_item = next(
        (query_item for query_item in query_items if "authorName" in query_item), 
        None
    )
    author_name = authorName_item.get("authorName").replace("%20", " ")
    sanitized_author_name = ' '.join(author_name.split())
    return sanitized_author_name


if __name__ == "__main__":
    app.run()