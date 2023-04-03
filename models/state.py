#!/usr/bin/python3
""" State Module for HBNB project """
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    @property
    def cities(self):
        cityList = []
        cities = storage.all(City)
        for city in cities.values():
            if self.id == city.state_id:
                cityList.append(city)
        return cityList
"""
#!/usr/bin/python3
""" holds class State"""
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list