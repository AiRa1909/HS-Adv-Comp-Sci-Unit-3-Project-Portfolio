from flask import Blueprint, render_template, redirect, url_for
from .models import Sesh

views = Blueprint('views', __name__)
# define as blueprint so that I can register it in __init__

@views.route('/')
def home():
    all_seshes = Sesh.query.filter(Sesh.duration > 0).all()
    # get durations of all finished sessions

    times = [s.duration for s in all_seshes]
    # extract in a list

    avg = round(sum(times) / len(times), 2) if times else 0
    #calculate average
    # the "if times" prevents crashing if the list is empty

    active = Sesh.query.filter_by(duration=None).first()
    # look for a session that has NO duration (the one currently running)

    return render_template("base.html", avg=avg, active=active)
# pass to base.html!!! (when it is rendered)
