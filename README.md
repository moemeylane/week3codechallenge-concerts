# week3codechallenge-concerts
Concert and Band Management Application
Overview
This application allows users to manage bands and their associated concerts. It provides functionality to create, read, and display information about bands and their performances.

Features
Create Band: Add new bands with their names and hometowns.
Create Concert: Schedule concerts for bands, specifying the concert name and date.
Display Information: Print out details of bands and their associated concerts.
Technologies Used
Python: Programming language for the application.
SQLAlchemy: ORM (Object Relational Mapping) tool for database management.
SQLite: Lightweight database for storing application data.
Pipenv: Dependency management tool for Python projects.
# Getting Started
Clone the repository:

`git@github.com:moemeylane/week3codechallenge-concerts.git`
cd `week3codechallenge-concerts`
Install dependencies using Pipenv:

`pipenv install`
Running the Application
Activate the Pipenv shell:
`pipenv shell`
Run the test methods to create and display bands and concerts:

`pipenv run python test_methods.py`
Example Output
yaml

'Band: The Rockers, Hometown: New York
Concert: Rock Fest, Date: 2024-10-01, Band ID: 1'
Code Structure
models.py: Contains the SQLAlchemy models for Band and Concert.
test_methods.py: Script to test the functionality of creating and displaying bands and concerts.
alembic/: Contains migration scripts for managing database schema changes.
