from api.extensions import db
from flask_login import UserMixin

class Musician(UserMixin, db.Model):
    mid = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    musician_name = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return f'<Musician {self.mid}: "{self.musician_name}">'
