from flask import request, jsonify, g
from http import HTTPStatus
from app.routes.authors.validations.index import validate_post_author_data
from app.routes.books.validations.index import validate_post_book_data

def validate_post_request_data():
    if request.path != '/books': return

    if request.method == 'POST':
        if not request.data:
            return jsonify(
                {"message": "Request body is empty"}
                ), HTTPStatus.BAD_REQUEST
        elif not request.is_json or not isinstance(request.json, dict):
            return jsonify(
                {"message": "Request body must be in JSON format"}
                ), HTTPStatus.BAD_REQUEST
        elif not len(request.json):
            return jsonify(
                {"message": "No data provided"}
                ), HTTPStatus.BAD_REQUEST
        try:
            if request.method == 'POST':
                if request.path == '/books':
                    g.validated_post_book_data = validate_post_book_data(request.json)
                elif request.path == '/authors':
                    g.validated_post_author_data = validate_post_author_data(request.json)
        except ValueError as e:
            return jsonify(
                {"message": f"Invalid data: {e}"}
                ), HTTPStatus.BAD_REQUEST