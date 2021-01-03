# classes with definitions of tables

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from database import Base


class Book(Base):
    __tablename__ = 'Book'

    ID = Column(Integer, primary_key=True)
    Title = Column(String(100), nullable=False)
    Value = Column(Integer)
    Author = Column(String(50))
    Description = Column(String(100))
    Type = Column(String(100))
    Content = Column(String(10000), nullable=False)

