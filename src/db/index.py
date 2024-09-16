from sqlalchemy.orm import sessionmaker
from db.init.index import init_struct
from cli.console.index import print_success,print_error

def create_session():
    engine = init_struct()
    connection = None
    if not engine:
        raise RuntimeError("Error! Database connection failed!")
    try:
        Session = sessionmaker(bind=engine)
        connection = Session()
        print_success("Database connection established successfully!")
    except Exception as e:
        print_error(f"An error occurred during session creation: {e}")
    return connection