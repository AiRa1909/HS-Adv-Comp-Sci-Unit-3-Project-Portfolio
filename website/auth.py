from flask import Blueprint, render_template, flash

auth = Blueprint('auth', __name__)

@auth.route("/")
def home():
    return render_template('base.html')