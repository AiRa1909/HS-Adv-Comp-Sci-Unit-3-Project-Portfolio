from flask import Blueprint, redirect, url_for, flash
from .models import Sesh
from . import db
from datetime import datetime

#btw, I wanted to keep the button routes here as they are post routes instead of the get route ("/") that gives the view of the web page to the user.

auth = Blueprint('auth', __name__)

@auth.route('/start', methods=['POST'])
def start():
    db.session.add(Sesh(start_time=datetime.now()))
    # create a new sesh entry with the current time
    db.session.commit()
    return redirect(url_for('views.home'))
    # go back to the home page to update


@auth.route('/stop', methods=['POST'])
def stop():
    active = Sesh.query.filter_by(duration=None).first()
    # find the sesh that is currently running
    if active:
        # calculate the difference between now and when it started
        diff = datetime.now() - active.start_time
        mins = round(diff.total_seconds() / 60, 2)
        # convert that time difference into minutes and round it
        active.duration = mins
        db.session.commit()
        # save the result to the database
        # db will mark it as finished

        flash(f"Congrats, your session ended! You studied for {mins} minutes just now.")
        # create a temporary message to show the user the time of the sesh they just finished
    return redirect(url_for('views.home'))