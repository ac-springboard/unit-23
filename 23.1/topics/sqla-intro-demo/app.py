"""Demo app using SQLAlchemy."""
import os

from flask import Flask, request, redirect, render_template

from models import db, connect_db, Pet
from seed import drop_create, insert_data

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///unit_23'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"


# debug = DebugToolbarExtension(app)

# seed
def seed():
    drop_create(db)
    insert_data(Pet, db)


if os.environ.get('SCHEMA_SEED') == 'True':
    seed()


@app.route("/")
def list_pets():
    """List pets and show add form."""

    pets = Pet.query.all()
    return render_template("list.html", pets=pets)


@app.route("/", methods=["POST"])
def add_pet():
    """Add pet and redirect to list."""

    name = request.form['name']
    species = request.form['species']
    hunger = request.form['hunger']
    hunger = int(hunger) if hunger else None

    pet = Pet(name=name, species=species, hunger=hunger)
    db.session.add(pet)
    db.session.commit()

    return redirect(f"/{pet.id}")


@app.route("/<int:pet_id>")
def show_pet(pet_id):
    """Show info on a single pet."""

    pet = Pet.query.get_or_404(pet_id)
    return render_template("detail.html", pet=pet)
