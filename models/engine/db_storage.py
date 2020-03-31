#!/usr/bin/python3
"""engine DBStorage
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import MetaData
import os
from models.base_model import Base


class DBStorage:

    __engine = None
    __session = None


    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        DBStorage.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db), pool_pre_ping=True)
        if user == 'test':
            Base.metadata.drop_all(DBStorage.__engine)


    def all(self, cls=None):
        all_dict = {}
        if cls is not None:
            for item in self.__session.query(cls.__name__):
                all_dict[cls.__name__ + "." + item.id] = item
        else:
            for table in metadata.tables.keys():
                for item in self.__session.query(table):
                    all_dict[table + "." + item.id] = item
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