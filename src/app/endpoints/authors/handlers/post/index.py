from http import HTTPStatus
from flask import g, jsonify
from services.authors.index import post_author

def post_authors_handler():
    try:
        author_data = g.validated_post_author_data
        author = post_author(author_data)
        return (
            jsonify({
                "author":author.to_dict()
            }), HTTPStatus.CREATED)
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during author creation: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)