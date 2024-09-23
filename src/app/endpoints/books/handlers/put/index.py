from http import HTTPStatus
from flask import jsonify, request
from app.endpoints.books.validations.index import validate_put_book_data
from services.books.index import get_book_by_bookId, put_book_by_bookId
from app.utils.index import handle_Integrity_Error

def put_book_by_id_handler(book_id):
    try:
        id = int(book_id)
        book = get_book_by_bookId(id)
        if not book:
            return jsonify(
                {"message": "Book not found"}
            ), HTTPStatus.NOT_FOUND
        book_to_update = book.to_dict()
        validated_data = validate_put_book_data(book_to_update, request.json)
        updated_book = put_book_by_bookId(book, validated_data)
        if not updated_book:
            return handle_Integrity_Error("A book with the same title already exists")
        return jsonify(
            {
                "book": updated_book.to_dict(),
                "message": "Book updated successfully"
            }), HTTPStatus.OK
    
    except ValueError as e:
        if str(e).startswith("invalid literal for int()"):
            return jsonify(
                {"message": "Invalid author ID"}
            ), HTTPStatus.BAD_REQUEST
        else:
            return jsonify(
                {"message": f"Validation error: {e}"}
            ), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify(
            {"message": f"An error occurred: {e}"}
        ), HTTPStatus.INTERNAL_SERVER_ERROR