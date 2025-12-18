from . import db
# import from __init__ :D

class Sesh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # primary key for unique id number for each sesh (btw sesh = study session)
    start_time = db.Column(db.DateTime)
    #store time at when the start button was pressed!

    duration = db.Column(db.Float)
    #then store total minutes.
