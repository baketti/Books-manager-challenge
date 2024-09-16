from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from utils.functions.index import disable_sqlalchemy_logging
import logging

Base = declarative_base()

def init_struct():
    disable_sqlalchemy_logging()
    engine = None
    try:
        engine = create_engine('sqlite:///db/books_authors.db', echo=True)
        print("Database 'books_authors' created successfully!")
        Base.metadata.create_all(engine)
        print("'books' and 'authors' tables created successfully!")
    except Exception as e:
        print(f"An error was occurred during database structure initialization: {e}")
    return engine

def disable_sqlalchemy_logging():
    logging.basicConfig()
    logging.getLogger('sqlalchemy').setLevel(logging.ERROR)
    logging.disable(logging.WARNING)
    logging.disable(logging.INFO)