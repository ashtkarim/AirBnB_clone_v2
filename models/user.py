#!usr/bin/python3
"""
Module:usr.py
"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    create new user
    """
    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', cascade="all,delete", back_populates="user")
        reviews = relationship('Review', cascade="all,delete", back_populates="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
