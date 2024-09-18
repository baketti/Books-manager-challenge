from db.models.DbConnection.index import DbConnection

def create_session():
    return DbConnection().get_connection()