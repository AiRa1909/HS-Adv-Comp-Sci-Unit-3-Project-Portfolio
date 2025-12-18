from flask import Blueprint, redirect, url_for, flash
from .models import Sesh
from . import db
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/start', methods=['POST'])
def start():
    db.session.add(Sesh(start_time=datetime.now()))
    db.session.commit()
    return redirect(url_for('views.home'))


@auth.route('/stop', methods=['POST'])
def stop():
    active = Sesh.query.filter_by(duration=None).first()
    if active:
        diff = datetime.now() - active.start_time
        mins = round(diff.total_seconds() / 60, 2)
        active.duration = diff.total_seconds() / 60
        db.session.commit()

        flash(f"Congrats, your session ended! You studied for {mins} minutes just now.")
    return redirect(url_for('views.home'))