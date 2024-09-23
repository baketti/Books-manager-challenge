from flask import jsonify, g
from services.books.index import post_book
from http import HTTPStatus
from app.utils.index import handle_Integrity_Error

def post_books_handler():
    try:
        book_data = g.validated_post_book_data
        book = post_book(book_data)
        if not book:
            return handle_Integrity_Error("A book with the same title already exists")
        return (jsonify({
            "book": book.to_dict(),
            "message": "Book created successfully"
        }), HTTPStatus.CREATED)
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during book creation: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)