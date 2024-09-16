from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db.init.index import Base

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=True)
    email = Column(String, unique=True, nullable=True)
    
    books = relationship("Book", back_populates="author")

    def __init__(self, name, birth_date=None, email=None):
        self.name = name
        self.birth_date = birth_date
        self.email = email
    
    def __repr__(self):
        return f"<Author(name={self.name}, birth_date={self.birth_date}, email={self.email})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_date": self.birth_date,
            "email": self.email
        }