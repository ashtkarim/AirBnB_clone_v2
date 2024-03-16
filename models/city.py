#!usr/bin/python
"""
Module:city.py
"""
import os
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel):
    """
    the city module
    """
    __tablename__ = 'cities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ''
        name = ''
