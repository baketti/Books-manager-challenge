from sqlalchemy.orm import sessionmaker
from db.init.index import init_struct

def create_session():
    engine = init_struct()
    connection = None
    if not engine:
        raise RuntimeError("Error! Database connection failed!")
    try:
        Session = sessionmaker(bind=engine)
        connection = Session()
        print("Database connection activated successfully!")
    except Exception as e:
        print(f"An error occurred during session creation: {e}")
    return connection