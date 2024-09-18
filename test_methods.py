from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Concert

# Create an SQLite in-memory database for testing
engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create a new Band
band1 = Band(name='The Rockers', hometown='New York')
session.add(band1)
session.commit()

# Create new Concert associated with the Band
concert1 = Concert(name='Rock Fest', date='2024-10-01', band_id=band1.id)
session.add(concert1)
session.commit()

# Query the data to verify the relationships
retrieved_band = session.query(Band).filter_by(name='The Rockers').first()
retrieved_concert = session.query(Concert).filter_by(name='Rock Fest').first()

print(f"Band: {retrieved_band.name}, Hometown: {retrieved_band.hometown}")
print(f"Concert: {retrieved_concert.name}, Date: {retrieved_concert.date}, Band ID: {retrieved_concert.band_id}")

# Close the session
session.close()
