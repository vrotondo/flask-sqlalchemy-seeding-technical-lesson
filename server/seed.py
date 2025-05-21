#!/usr/bin/env python3
#server/seed.py

from app import app
from models import db, Pet

with app.app_context():

    # Delete all rows in the "pets" table
    Pet.query.delete()

    # Create an empty list
    pets = []

    # Add some Pet instances to the list
    pets.append(Pet(name = "Fido", species = "Dog"))
    pets.append(Pet(name = "Whiskers", species = "Cat"))
    pets.append(Pet(name = "Hermie", species = "Hamster"))
    pets.append(Pet(name = "Slither", species = "Snake"))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()