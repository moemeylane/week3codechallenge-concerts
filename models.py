from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# Base class for declarative class definitions
Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    # one-to-many relationship with Concert
    concerts = relationship("Concert", back_populates="band")

class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    # one-to-many relationship with Concert
    concerts = relationship("Concert", back_populates="venue")

class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    # many-to-one relationships
    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")
