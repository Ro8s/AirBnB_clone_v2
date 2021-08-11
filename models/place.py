#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    metadata = Base.metadata

    place_amenity = Table('association', metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False))

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if (getenv('HBNB_TYPE_STORAGE') == "db"):
        reviews = relationship('Review', backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship('Amenity',
                                 secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """ The relationship of Review """
            from models import storage
            from models.review import Review
            my_place = {}
            for review, value in storage.all(Review).items():
                if (value.place_id == self.id):
                        my_place.update({review: value})
            return my_place

        @property
        def amenities(self):
            """ The relationship of Review """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, input):
            """ The relationship setter of Review """
            if (type(value) != Amenity):
                return
            self.amenity_ids = []
            new_amenities = storage.all(Amenity)
            for key in new_amenities:
                if new_amenities[key].amenity_id == self.id:
                    self.amenity_ids.append(new_amenities[key].id)
