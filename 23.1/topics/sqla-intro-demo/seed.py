"""Seed file to make sample data for pets db."""


# from models import Pet, db

def drop_create(db):
    # Create all tables
    db.drop_all()
    db.create_all()


# If table isn't empty, empty it
# Pet.query.delete()

def insert_data(pet, db):
    # Add pets
    whiskey = pet(name='Whiskey', species="dog")
    bowser = pet(name='Bowser', species="dog", hunger=10)
    spike = pet(name='Spike', species="porcupine")

    # Add new objects to session, so they'll persist
    db.session.add(whiskey)
    db.session.add(bowser)
    db.session.add(spike)

    # Commit--otherwise, this never gets saved!
    db.session.commit()
