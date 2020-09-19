from my_app import app,models
from flask import render_template, request, redirect
import requests

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
