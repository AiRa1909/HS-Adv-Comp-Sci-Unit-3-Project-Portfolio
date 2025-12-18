from . import db

class Sesh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    duration = db.Column(db.Float)