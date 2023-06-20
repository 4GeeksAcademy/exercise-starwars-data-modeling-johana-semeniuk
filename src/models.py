import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False) 
    password = Column(String(250), nullable=False)

class PlanetFavorite(Base):
    __tablename__ = 'planet_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet')

class CharacterFavorite(Base):
    __tablename__ = 'character_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Character')

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False) 
    population = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False) 
    birth_year = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    starship = Column(String(250), nullable=False)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)


    people_id = Column(Integer, ForeignKey('people.id'))
    people= relationship(People)

    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets= relationship(Planets)

    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles= relationship(Vehicles)

    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')