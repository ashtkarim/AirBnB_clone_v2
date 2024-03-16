#!/usr/bin/python3
"""
Module:base_model.py
"""
import models
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
Base = declarative_base()


class BaseModel():
    """
    create class BaseModel
    """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        initalisation of an object with it's
        attributes
        Args :
                Args(won't be used ): list of arguments
                Kwargs: pass in dictionary as arguments
        """
        if kwargs:
            for key, v in kwargs.items():
                if key != '__class__':
                    setattr(self, key, v)
                elif key in ('created_at', 'updated_at'):
                    Nv = datetime.fromisoformat(v)
                    setattr(self, key, Nv)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        return the string of instences
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        update updated_at
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        to_dict methode
        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        for key, value in self.__class__.items():
            dict[key] = value
            if key in ['created_at', 'updated_at']:
                dict[key] = value.isoformat()
        dict.pop('_sa_instance_state', None)

        # if isinstance(self.created_at, datetime):
        #     dict['created_at'] = self.created_at.isoformat()
        # else:
        #     dict['created_at'] = self.created_at
        # if isinstance(self.updated_at, datetime):
        #     dict['updated_at'] = self.updated_at.isoformat()
        # else:
        #     dict['updated_at'] = self.updated_at
        return dict

    def delete(self):
        """
        delete theh currect intence from storage
        """
        models.storage.delete(self)
