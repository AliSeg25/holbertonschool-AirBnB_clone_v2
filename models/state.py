#!/usr/bin/python3
""" State Module for HBNB project """
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):

        if models.storage_t == "db":
            cityList = []
            for city in self.cities:
                cityList.append(city)
            return cityList
        else:
            cityList = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cityList.append(city)
            return cityList
"""
#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City  # Ajout de cette ligne pour importer City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):

        if type(models.storage).__name__ == "DBStorage":
            cityList = []
            for city in self.cities:
                cityList.append(city)
            return cityList
        else:
            cityList = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cityList.append(city)
            return cityList
