from flask import jsonify
from services.books.index import get_book_by_bookId, delete_book_by_bookId
from http import HTTPStatus

def delete_book_by_id_handler(book_id):
    try:
        id = int(book_id)
        book = get_book_by_bookId(id)
        if not book:
            return (
                jsonify({
                    "message": "No book found"
                }), HTTPStatus.NOT_FOUND)
        delete_book_by_bookId(id)
        return (
            jsonify({
                "message": "Book deleted successfully"
            }), HTTPStatus.OK
        )
    except Exception as e:
        print("Error", e)
        return jsonify({
            "message": "Invalid book ID"
        }), HTTPStatus.BAD_REQUEST