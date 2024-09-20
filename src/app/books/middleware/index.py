from flask import request, jsonify, g
from http import HTTPStatus
from app.books.validations.index import validate_post_book_data

def validate_books_request_data():
    if request.path != '/books': return

    if request.method == 'POST' or request.method == 'PUT':
        if not request.data:
            return jsonify(
                {"message": "Request body is empty"}
                ), HTTPStatus.BAD_REQUEST
        elif not request.is_json or not isinstance(request.json, dict):
            return jsonify(
                {"message": "Request body must be in JSON format"}
                ), HTTPStatus.BAD_REQUEST
        elif not len(request.json):
            print("No data provided")
            return jsonify(
                {"message": "No data provided"}
                ), HTTPStatus.BAD_REQUEST
        try:
            if request.method == 'POST':
                g.validated_data = validate_post_book_data(request.json)
        except ValueError as e:
            return jsonify(
                {"message": f"Invalid data: {e}"}
                ), HTTPStatus.BAD_REQUEST