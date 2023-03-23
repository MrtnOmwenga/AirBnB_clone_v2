#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
#from models.city import City
from sqlalchemy import Column, String
import models
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if models.HBNB_TYPE_STORAGE == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name=""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.HBNB_TYPE_STORAGE != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            from models.city import City
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
