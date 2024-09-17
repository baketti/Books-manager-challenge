from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.init.index import Base
from services.authors.index import get_author_by_authorId

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id', ondelete="RESTRICT"), nullable=False)
    pages = Column(Integer)
    price = Column(Float)
    publisher = Column(String)
    
    author = relationship("Author", back_populates="books")

    def __init__(self, title, author_id, pages=None, price=None, publisher=None):
        self.title = title
        self.author_id = author_id
        self.pages = pages
        self.price = price
        self.publisher = publisher
    
    def __repr__(self):
        return f"<Book(title={self.title}, authorID={self.author_id}, pages={self.pages}, price={self.price}, publisher={self.publisher})>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author_id,
            "pages": self.pages,
            "price": self.price,
            "publisher": self.publisher
        }
