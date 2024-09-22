from flask import request
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