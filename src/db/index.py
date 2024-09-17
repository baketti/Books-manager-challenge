from sqlalchemy.orm import sessionmaker
from db.init.index import init_struct
from cli.console.index import print_success,print_error
from db.models.DbConnection.index import DbConnection

def create_session():
    return DbConnection().get_connection()