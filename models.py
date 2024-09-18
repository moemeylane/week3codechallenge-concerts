from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# base class for declarative class definitions
Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    # one-to-many relationship with Concert
    concerts = relationship("Concert", back_populates="band")

class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'))

    # many-to-one relationship with Band
    band = relationship("Band", back_populates="concerts")
