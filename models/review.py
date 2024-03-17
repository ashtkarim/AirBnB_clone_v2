#!/usr/bin/python3
"""
Module:review.py
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv

class Review(BaseModel):
    """
    review class
    """
    text = ""
    user_id = ""
    place_id = ""
    """new class attributes"""
    __tablename__ = 'reviews'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
