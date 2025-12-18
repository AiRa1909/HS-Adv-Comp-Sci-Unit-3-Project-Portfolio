from flask import Blueprint, render_template, redirect, url_for
from .models import Sesh

views = Blueprint('views', __name__)


@views.route('/')
def home():
    # Get durations of all finished sessions
    all_seshes = Sesh.query.filter(Sesh.duration > 0).all()
    times = [s.duration for s in all_seshes]

    avg = round(sum(times) / len(times), 2) if times else 0

    active = Sesh.query.filter_by(duration=None).first()

    return render_template("base.html", avg=avg, active=active)
