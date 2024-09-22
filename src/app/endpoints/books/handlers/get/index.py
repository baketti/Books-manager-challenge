from flask import request, jsonify
from app.utils.index import get_limit_query_param
from services.books.index import get_all_books, get_book_by_bookId, get_books_by_authorId
from services.authors.index import get_authors_by_authorName
from utils.index import sanitize_string
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
            "book":book.to_dict()
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
            books = [book.to_dict() for book in get_all_books(limit)]
        else:
            authors = get_authors_by_authorName(author_name, is_search=True)
            for author in authors:
                books.append({
                    "author_name": author.name,
                    "books": [book.to_dict() for book in get_books_by_authorId(author.id)]
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
