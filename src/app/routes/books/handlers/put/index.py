from http import HTTPStatus
from flask import jsonify, request
from app.routes.books.validations.index import validate_put_book_data
from services.books.index import get_book_by_bookId, put_book_by_bookId

def put_book_by_id_handler(conn, book_id):
    try:
        id = int(book_id)
        book = get_book_by_bookId(conn, id)
        if not book:
            return jsonify(
                {"message": "Book not found"}
                ), HTTPStatus.NOT_FOUND
        book_to_update = book.to_dict()
        validated_data = validate_put_book_data(book_to_update, request.json)
        updated_book = put_book_by_bookId(conn, book, validated_data)
        return jsonify(
            {
                "message": "Book updated successfully",
                "book": updated_book.to_dict()
            }), HTTPStatus.OK
    
    except ValueError as ve:
        if str(ve).startswith("invalid literal for int()"):
            return jsonify(
                {"message": "Invalid author ID"}
            ), HTTPStatus.BAD_REQUEST
        else:
            return jsonify(
                {"message": f"Validation error: {ve}"}
            ), HTTPStatus.BAD_REQUEST
        
    except Exception as e:
        return jsonify(
            {"message": f"An error occurred: {e}"}
        ), HTTPStatus.INTERNAL_SERVER_ERROR