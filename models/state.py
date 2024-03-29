#!/usr/bin/python3
"""
Module:state.py
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """
    state class
    """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')
    else:
        name = ""


    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            getter attribute
            """
            from models import storage
            match_cities = []
            all_cities = models.storage.all(City).value()
            for city in all_cities:
                if city.state_id == self.id:
                    match_cities.append(city)
            return match_cities
