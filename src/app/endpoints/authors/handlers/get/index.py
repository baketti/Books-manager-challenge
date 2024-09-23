from flask import jsonify
from services.authors.index import get_all_authors, get_author_by_authorId
from http import HTTPStatus
from app.utils.index import get_limit_query_param
from utils.index import convert_to_dict_list

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
        return (jsonify({
            "author": author.to_dict()
        }), HTTPStatus.OK)
    
    except Exception as e:
        return jsonify({
            "message": "Invalid author ID"
        }), HTTPStatus.BAD_REQUEST

def get_authors_handler():
    try: 
        limit = get_limit_query_param()
        authors = get_all_authors(limit)
        if not authors:
            return (
                jsonify({
                    "message": "No authors found"
                }), 
                HTTPStatus.NOT_FOUND)
        return (
            jsonify({
                "authors": convert_to_dict_list(authors)
            }), HTTPStatus.OK)
    
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during authors retrieval: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)