from sqlalchemy import create_engine
from models import Base

# Create an SQLite database and tables
engine = create_engine('sqlite:///concerts.db')
Base.metadata.create_all(engine)
