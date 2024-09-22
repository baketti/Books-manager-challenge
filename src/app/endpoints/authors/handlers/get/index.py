from flask import jsonify
from services.authors.index import get_all_authors, get_author_by_authorId
from http import HTTPStatus

def get_author_by_id_handler(book_id):
    try:
        id = int(book_id)
        author = get_author_by_authorId(id)
        if not author:
            return (
                jsonify({
                    "message": "No author found"
                }), 
                HTTPStatus.NOT_FOUND)
        return (
            jsonify(author.to_dict()),
            HTTPStatus.OK
        )
    except Exception as e:
        return jsonify({
            "message": "Invalid author ID"
        }), HTTPStatus.BAD_REQUEST

# TODO implement search by email (?)
def get_authors_handler():
    try: 
        authors = get_all_authors()
        if not authors:
            return (
                jsonify({
                    "message": "No authors found"
                }), 
                HTTPStatus.NOT_FOUND)
        return (
            jsonify({
                "authors":[author.to_dict() for author in authors]
            }), HTTPStatus.OK)
    
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during books retrieval: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)