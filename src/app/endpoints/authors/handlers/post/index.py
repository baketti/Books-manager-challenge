from http import HTTPStatus
from flask import g, jsonify
from services.authors.index import post_author
from app.utils.index import handle_Integrity_Error

def post_authors_handler():
    try:
        author_data = g.validated_post_author_data
        author = post_author(author_data) 
        if not author:
            return handle_Integrity_Error("An author with the same name or email already exists")
        return (
            jsonify({
                "author":author.to_dict(),
                "message": "Author created successfully"
            }), HTTPStatus.CREATED)
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during author creation: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)