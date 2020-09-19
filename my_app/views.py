from my_app import app
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
    if (signup_request == None):
        return render_template("error.html",msg="Oops. Incomplete form!")

    # check database to see if there's a username match.
    if (acc != None): # if there is a match
        return render_full_template("error.html",msg="There's already an account by that name!")
        # return an error
    db.execute("INSERT INTO users (username,password) VALUES (:user,:pw)", {"user":signup_request[0],"pw":signup_request[1]})
    db.commit()
    acc = db.execute("SELECT * FROM users WHERE username = :username", {'username': signup_request[0]}).fetchone()
    session["user"] = acc.id
    return redirect("/")

@app.route("/dates/")
def view_dates():
    # see all dates !

    return render_template("dates.html")


@app.route("/users")
def view_users():
    return render_template("users.html")



@app.route("/user/<id>")
def view_one_user(id):
    user = None  # USE ID TO FETCH FROM DB
    return render_template("user.html",user=user)
