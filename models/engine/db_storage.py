#!/usr/bin/python3
"""engine DBStorage
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import MetaData
import os
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        d_sql = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db)
        DBStorage.__engine = create_engine(d_sql, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        class_list = [User, State, City, Amenity, Place, Review]
        all_dict = {}
        if cls is not None:
            class_obj = eval(cls)
            for item in self.__session.query(class_obj):
                if '_sa_instance_state' in item.__dict__.keys():
                    del item.__dict__['_sa_instance_state']
                all_dict[cls + "." + item.id] = item
        else:
            for table in class_list:
                for item in self.__session.query(table):
                    if '_sa_instance_state' in item.__dict__.keys():
                        del item.__dict__['_sa_instance_state']
                    all_dict[table.__class__.__name__ + "." + item.id] = item
        return all_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
