from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

words_database = declarative_base()

class Difficulty(words_database):
    """Difficulty class for the database

    Args:
        words_database (database): Base class for SQLAlchemy models
    """
    __tablename__ = 'difficulty'

    id = Column(Integer, primary_key=True)
    difficulty = Column(String)

class Category(words_database):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category = Column(String)

class Word(words_database):
    __tablename__ = 'word'

    id = Column(Integer, primary_key=True)
    category = Column(String, ForeignKey('category.id'))
    difficulty = Column(Integer, ForeignKey('difficulty.id'))
    word = Column(String)