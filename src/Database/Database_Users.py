"""Module for managing user data in the database"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# ============== USERS ==================

users_database = declarative_base()


class User(users_database):
    """Class for users in the database

    Args:
        users_database (type): Base class for SQLAlchemy models
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String)
    name = Column(String)
    password = Column(String)

    # so like, bro you work with "Stats", also tell Stats that they work with "User" and you shouldn't make stats a list, ok?
    stats = relationship("Stats", back_populates="user", uselist=False)


class Stats(users_database):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    games_played = Column(Integer)
    games_won = Column(Integer)
    total_time = Column(String)

    user = relationship("User", back_populates="stats")
