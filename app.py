"""Pet adoption flask app."""

from flask import Flask, render_template, redirect, flash, url_for, jsonify

# commenting out the DebugToolbar cause it's causing error
# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "petsarecute"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)


@app.cli.command("create_db")
def create_db():
    """Create the database tables."""
    db.create_all()
    print("Database tables created.")

# commenting out the DebugToolbar cause it's causing error
# toolbar = DebugToolbarExtension(app)


@app.route("/")
def pets_page():
    """Homepage--show a list of all pets."""

    pets = Pet.query.all()
    return render_template("pets_page.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a new pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {key: value for key, value in form.data.items()
                if key != "csrf_token"}
     #    Pet(**data) is a shortcut syntax to get info such as form.name.data, form.age.data, etc.
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added!")
        return redirect(url_for('pets_page'))

    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit a pet's info."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data

        db.session.commit()
        flash(f"{pet.name} has been updated!")
        return redirect(url_for('pets_page'))

    else:
        return render_template("edit_pet_form.html", pet=pet, form=form)


if __name__ == '__main__':
    app.run(debug=True)
