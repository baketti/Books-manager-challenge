from http import HTTPStatus
from flask import g, jsonify
from services.authors.index import post_author

def post_authors_handler(conn):
    try:
        if g.validated_post_author_data:# controlla perche dovrebbe non essere necessario questo if
            author_data = g.validated_post_author_data
            print(author_data)    
            book = post_author(conn, author_data)
            return (
                jsonify(book.to_dict()),
                HTTPStatus.CREATED)
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during author creation: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)