from flask import request, jsonify
from services.authors.index import get_author_by_authorId, delete_author_by_authorId
from http import HTTPStatus

def delete_author_by_id_handler(conn, author_id):
    try:
        id = int(author_id)
        author = get_author_by_authorId(conn, id)
        if not author:
            return (
                jsonify({
                    "message": "No author found"
                }),
                HTTPStatus.NOT_FOUND)
        delete_author_by_authorId(conn, id)
        return (
            jsonify({
                "message": "Author deleted successfully"
            }),
            HTTPStatus.OK
        )
    except ValueError as e:
        return jsonify({
            "message": "Invalid author ID"
        }), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({
            "message": f"An error occurred during author deletion: {e}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR