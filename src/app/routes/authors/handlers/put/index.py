from http import HTTPStatus
from flask import jsonify, request
from app.routes.authors.validations.index import validate_put_author_data
from services.authors.index import get_author_by_authorId, put_author_by_authorId

def put_author_by_id_handler(conn, author_id):
    try:
        id = int(author_id)
        author = get_author_by_authorId(conn, id)
        if not author:
            return jsonify(
                {"message": "Author not found"}
                ), HTTPStatus.NOT_FOUND
        
        author_to_update = author.to_dict()
        validated_data = validate_put_author_data(author_to_update, request.json)
        updated_author = put_author_by_authorId(conn, id, validated_data)
        return jsonify(
            {
                "message": "Author updated successfully",
                "author": updated_author.to_dict()
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