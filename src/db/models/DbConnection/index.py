from db.init.index import init_struct
from cli.console.index import print_success, print_error
from sqlalchemy.orm import sessionmaker

class DbConnection:
    _instance = None
    _connection = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DbConnection, cls).__new__(cls)
            cls._initialize_connection()
        return cls._instance
    
    @classmethod
    def _initialize_connection(cls):
        engine = init_struct()
        if not engine:
            raise RuntimeError("Error! Database connection failed!")
        try:
            Session = sessionmaker(bind=engine)
            cls._connection = Session()
            print_success("Database connection established successfully!")
        except Exception as e:
            print_error(f"An error occurred during session creation: {e}")

    @classmethod
    def get_connection(cls):
        return cls._connection