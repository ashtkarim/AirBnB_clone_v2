#!/usr/bin/python3
"""
Module:state.py
"""
import os
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel):
    """
    state class
    """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City')
    else:
        name = ""

        def cities(self):
            """
            getter attribute
            """
            match_cities = []
            all_cities = models.storage.all(City).value()
            for city in all_cities:
                if city.state_id == self.id:
                    match_cities.append(city)
            return match_cities
