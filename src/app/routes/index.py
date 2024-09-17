from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from app.routes.books.index import books_bp
        app.register_blueprint(books_bp)
    return app

app = create_app()