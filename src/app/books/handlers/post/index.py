from flask import jsonify, g
from services.books.index import post_book
from http import HTTPStatus

def post_books_handler(conn):
    try:
        if g.validated_data:# controlla perche dovrebbe non essere necessario questo if
            book_data = g.validated_data
            print(book_data)    
            book = post_book(conn, book_data)
            return (
                jsonify(book.to_dict()),
                HTTPStatus.CREATED)
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during book creation: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)