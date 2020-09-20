import os

from flask import Flask, render_template, request, redirect, jsonify
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

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/complete")
def complete():
    return render_template("complete.html")

@app.route("/useradd",methods=["POST"])
def add_user():
    """
    Signup attempts are routed here — either inserted or rejected
    """

    name = request.form.get("name")
    email = request.form.get("email")

    print(name)
    print(email)

    u = User(name=name, email=email,phone="000000000",openness=1,consc=2,extraversion=3,agreeable=4,neuroticism=5,major="Undeclared")
    db.session.add(u)
    db.session.commit()
    return redirect("/complete")


@app.route("/dates",methods=["GET","POST"])
def view_dates():
    # see all dates !
    if (request.method == "POST"):
        date_id = request.form.get("date_id")
        user_id = request.form.get("user_id")
        date = Date.query.get(date_id)
        date.add_person(user_id)



    """List all Dates."""
    dates = Date.query.all()
    users = User.query.all()
    return render_template("dates.html",dates=dates,users=users)


@app.route("/users")
def view_users():
    """List all users."""
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/users/<int:user_id>")
def view_one_user(user_id):
    user = User.query.get(user_id) # USE ID TO FETCH FROM DB
    if (user == None):
        return render_template("error.html",msg="Can't find a person by that id!")
    return render_template("user.html",user=user)
