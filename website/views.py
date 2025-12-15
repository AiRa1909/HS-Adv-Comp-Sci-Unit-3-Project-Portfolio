from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)