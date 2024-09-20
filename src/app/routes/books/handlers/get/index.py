from flask import request, jsonify
from services.books.index import get_all_books, get_books_by_authorName, get_book_by_bookId
from utils.index import sanitize_string
from http import HTTPStatus

def get_book_by_id_handler(conn,book_id):
    try:
        id = int(book_id)
        book = get_book_by_bookId(conn,id)
        if not book:
            return (
                jsonify({
                    "message": "No book found"
                }), 
                HTTPStatus.NOT_FOUND)
        return (
            jsonify(book.to_dict()),
            HTTPStatus.OK
        )
    except Exception as e:
        print("Error", e)
        return jsonify({
            "message": "Invalid book ID"
        }), HTTPStatus.BAD_REQUEST

def get_books_handler(conn):
    books = None
    try:
        query_params = request.query_string.decode()

        if not query_params: 
            books = get_all_books(conn)
        else:
            author_name = get_authorName_query_param()
            books = get_books_by_authorName(conn, author_name)

        if not books:
            return (
                jsonify({
                    "message": "No books found"
                }), 
                HTTPStatus.NOT_FOUND)
        
        return (
            jsonify([book.to_dict() for book in books]),
            HTTPStatus.OK)
    
    except Exception as e:
        return (
            jsonify({
                "message": f"An Internal Error occurred during books retrieval: {e}"
            }),HTTPStatus.INTERNAL_SERVER_ERROR)

def get_authorName_query_param():
    author_name = request.args.get('authorName')
    sanitized_author_name = sanitize_string(author_name)
    return sanitized_author_name