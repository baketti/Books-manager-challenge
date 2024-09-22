from flask import jsonify, g
from services.books.index import post_book
from http import HTTPStatus

def post_books_handler():
    try:
        book_data = g.validated_post_book_data
        book = post_book(book_data)
        return (jsonify({
            "book": book.to_dict()
        }), HTTPStatus.CREATED)
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during book creation: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)