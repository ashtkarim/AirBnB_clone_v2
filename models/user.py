#!usr/bin/python3
"""
Module:usr.py
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    create new user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    """new attributes"""
    __tablename__ = 'users'
    email =  Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name =  Column(String(128), nullable=False)
    places = relationship('place',
             backref=backref("user", cascade="all, delete-orphan")
