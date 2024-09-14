from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

def init_struct():
    engine = None
    try:
        engine = create_engine('sqlite:///db/books_authors.db', echo=True)
        print("Database 'books_authors' created successfully!")
        Base.metadata.create_all(engine)
        print("'books' and 'authors' tables created successfully!")
    except Exception as e:
        print(f"An error was occurred during database structure initialization: {e}")
    return engine