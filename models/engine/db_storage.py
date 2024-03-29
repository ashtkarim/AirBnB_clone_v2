#!/usr/bin/python3
"""define DBStorage class"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity


classes = {"State": State, "City": City, "User": User,
        "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    """private attributes"""

    __engine = None
    __session = None

    def __init__(self):
        """initialize a new instance of DBSorgae Class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """  """
        all_classes = {
            "State": State,
            "City": City,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }
        new_dict = {}
        for clss in all_classes:
            if cls is None or cls == all_classes[clss] or cls == clss:
                objs = self.__session.query(all_classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and
        the current database session """
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session()

    def close(self):
        """ call remove() method on the private session attribute
        (self.__session)or close() on the class Session tips """
        self.__session.close()
