# Here we save route for our page
from flask import Blueprint, render_template


views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template('sql_data.html')
