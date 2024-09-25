import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

class TestConcertDatabase(unittest.TestCase):

    def setUp(self):
        # Setup an in-memory database for testing
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Create a test band and venue
        self.band = Band(name='The Rockers', hometown='New York')
        self.venue = Venue(title='Madison Square Garden', city='New York')
        self.session.add(self.band)
        self.session.add(self.venue)
        self.session.commit()

    def tearDown(self):
        self.session.close()

    def test_create_concert(self):
        # Create a concert linked to the band and venue
        concert = Concert(name='Rock Fest', date='2024-10-01', band_id=self.band.id, venue_id=self.venue.id)
        self.session.add(concert)
        self.session.commit()

        # Retrieve and assert the concert and its relationships
        retrieved_concert = self.session.query(Concert).filter_by(name='Rock Fest').first()
        self.assertIsNotNone(retrieved_concert)
        self.assertEqual(retrieved_concert.band.name, 'The Rockers')
        self.assertEqual(retrieved_concert.venue.title, 'Madison Square Garden')

    def test_retrieve_band(self):
        retrieved_band = self.session.query(Band).filter_by(name='The Rockers').first()
        self.assertEqual(retrieved_band.hometown, 'New York')

    def test_retrieve_venue(self):
        retrieved_venue = self.session.query(Venue).filter_by(title='Madison Square Garden').first()
        self.assertEqual(retrieved_venue.city, 'New York')

if __name__ == '__main__':
    unittest.main()
