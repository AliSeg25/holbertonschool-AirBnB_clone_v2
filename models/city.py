#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import DateTime

created_at = Column(DateTime, nullable=False)
updated_at = Column(DateTime, nullable=False)

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    id = Column(String(36), primary_key=True)

    places = relationship('Place', cascade='all, delete', backref='cities', overlaps="cities")