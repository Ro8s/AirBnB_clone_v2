#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from models.user import User
from models.place import Place


class Amenity(BaseModel, Base):
    """Amenity"""
    __tablename__ = 'amenities'
    name = Column(String(), nullable=False)
    place_amenities = relationship('Place', secondary=association_table)
