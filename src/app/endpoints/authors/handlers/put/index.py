from http import HTTPStatus
from flask import jsonify, request
from app.endpoints.authors.validations.index import validate_put_author_data
from services.authors.index import get_author_by_authorId, put_author_by_authorId
from app.utils.index import handle_Integrity_Error

def put_author_by_id_handler(author_id):
    try:
        id = int(author_id)
        author = get_author_by_authorId(id)
        if not author:
            return jsonify(
                {"message": "Author not found"}
                ), HTTPStatus.NOT_FOUND
        
        author_to_update = author.to_dict()
        validated_data = validate_put_author_data(author_to_update, request.json)
        updated_author = put_author_by_authorId(id, validated_data)
        if not updated_author:
            return handle_Integrity_Error("An author with the same name or email already exists")
        return jsonify(
            {
                "author": updated_author.to_dict(),
                "message": "Author updated successfully"
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