from http import HTTPStatus
from flask import jsonify, request
from utils.index import sanitize_string

def get_limit_query_param():
    author_name = request.args.get('limit')
    limit = sanitize_string(author_name)
    if not limit:
        return None
    try:
        return int(limit)
    except ValueError:
        raise ValueError("invalid limit value. Limit must be an integer")
    
def handle_Integrity_Error(msg: str):
    # This is to return a correct response message.
    # Unique constraint errors are handled in the services, but for a specific reason, they aren't raised.
    # (the reason is that I don't like error messages when data imported from csv already exist...)
    # Because of this, IntegrityError can't be handled directly.
    # Therefore, we handle them by returning a correct response message.
    # When the request reaches the endpoint and the post or put service is called, 
    # if the item is None, it is only because it already exists,
    # since the data is validated before reaching this point.
    return (
        jsonify({
            "message": msg
        }), HTTPStatus.CONFLICT)