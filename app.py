"""Pet adoption flask app."""

from flask import Flask, render_template, redirect, flash

# commenting out the DebugToolbar cause it's causing error
# from flask_debugtoolbar import DebugToolbarExtension

from models
from forms

app = Flask(__name__)

app.config['SECRET_KEY'] = "petsarecute"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# commenting out the DebugToolbar cause it's causing error
# toolbar = DebugToolbarExtension(app)