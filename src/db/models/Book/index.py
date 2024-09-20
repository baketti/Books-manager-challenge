from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.init.index import Base

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id', ondelete="RESTRICT"), nullable=False)
    pages = Column(Integer)
    price = Column(Float)
    publisher = Column(String)
    category = Column(String)
    
    author = relationship("Author", back_populates="books")

    def __init__(self, title, author_id, pages=None, price=None, publisher=None, category=None):
        self.title = title
        self.author_id = author_id
        self.pages = pages
        self.price = price
        self.publisher = publisher
        self.category = category
    
    def __repr__(self):
        return f"<Book(title={self.title}, authorID={self.author_id}, pages={self.pages}, price={self.price}, publisher={self.publisher}), category={self.category}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author_id,
            "pages": self.pages,
            "price": self.price,
            "publisher": self.publisher,
            "category": self.category
        }
