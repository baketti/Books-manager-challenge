from flask import request, jsonify
from app.utils.index import get_limit_query_param
from services.books.index import get_all_books, get_book_by_bookId, get_books_by_authorId
from services.authors.index import get_authors_by_authorName
from utils.index import sanitize_string, convert_to_dict_list
from http import HTTPStatus

def get_book_by_id_handler(book_id):
    try:
        id = int(book_id)
        book = get_book_by_bookId(id)
        if not book:
            return (
                jsonify({
                    "message": "No book found"
                }), 
                HTTPStatus.NOT_FOUND)
        return (jsonify({
            "book": book.to_dict()
        }), HTTPStatus.OK)
    except Exception as e:
        return jsonify({
            "message": "Invalid book ID"
        }), HTTPStatus.BAD_REQUEST

def get_books_handler():
    books = []
    try:
        author_name = get_authorName_query_param()
        limit = get_limit_query_param()
        if not author_name:
            book_list = get_all_books(limit) 
            books = convert_to_dict_list(book_list)
        else:
            authors = get_authors_by_authorName(author_name, is_search=True)
            if authors:
                for author in authors:
                    book_list = get_books_by_authorId(author.id, limit)
                    books.append({
                        "author_name": author.name,
                        "books": convert_to_dict_list(book_list)
                    })
        if not len(books):
            return (
                jsonify({
                    "message": "No books found"
                }), HTTPStatus.NOT_FOUND)
        return (
            jsonify({
                "list": books
            }), HTTPStatus.OK)
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during books retrieval: {e}"
            }), HTTPStatus.INTERNAL_SERVER_ERROR)

def get_authorName_query_param():
    author_name = request.args.get('authorName')
    sanitized_author_name = sanitize_string(author_name)
    return sanitized_author_name