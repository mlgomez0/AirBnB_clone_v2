#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
import models

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref='state')
    else:
        @property
        def cities(self):
            """returns the list of City instances
            """
            obj_l = []
            ints = models.storage.all()
            for k, v in ints.items():
                if k.split(".")[0] == "City" and v.state_id == self.id:
                    obj_l.append(v)
            return obj_l
