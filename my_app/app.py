import os

from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from models import *


base = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post_user",methods=["POST"])
def add_user():
    """
    Signup attempts are routed here—either inserted or rejected
    """
    signup_request = request.form.get("name")
    #if some form variables don't exist or

    return redirect("/",msg="Success! We will communicate further with you once we've found a match.")


@app.route("/dates/")
def view_dates():
    # see all dates !
    """List all Dates."""
    dates = Date.query.all()
    return render_template("dates.html",dates=dates)


@app.route("/users")
def view_users():
    """List all users."""
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/user/<int:user_id>")
def view_one_user(user_id):
    user = User.query.get(user_id) # USE ID TO FETCH FROM DB
    return render_template("user.html",user=user)
