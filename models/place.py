#!/usr/bin/python3
"""
Module:place.py
"""
from os import getenv
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Place(BaseModel):
    """
    class place
    """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullabel=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        name = ""
        user_id = ""
        city_id = ""
        description = ""
        number_bathrooms = 0
        price_by_night = 0
        number_rooms = 0
        longitude = 0.0
        latitude = 0.0
        max_guest = 0
        amenity_ids = []
