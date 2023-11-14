"""Models for the adopt flask app."""

from flask_sqlalchemy import SQLAlchemy

"""Models for adopt app."""


GENERIC_IMAGE = "https://i.giphy.com/media/j2Brn3luUP7BxLdgvB/200w.gif"

db = SQLAlchemy()


class Pet(db.Model):
    """Pet available to be adopted."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Pet image."""

        return self.photo_url or GENERIC_IMAGE


def connect_db(app):
    """Connect this database to provided Flask app. Call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
