import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import import_fake


base = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)

    # contact info
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    # personality characteristics
    openness = db.Column(db.Integer())
    consc = db.Column(db.Integer()) # conscientiousness
    extraversion = db.Column(db.Integer())
    agreeable = db.Column(db.Integer())
    neuroticism = db.Column(db.Integer())
    # major?
    major = db.Column(db.String)
    # interests ?
    date_id = db.Column(db.Integer, db.ForeignKey("scheduled_dates.id"), nullable=True)
    # null before the person is assigned a meeting time

class Date(db.Model):
    __tablename__ = "scheduled_dates"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    description = db.Column(db.String(800))
    link = db.Column(db.String(100))


    time_descriptor = db.Column(db.String(10))
    users = db.relationship("User", backref="date", lazy=True)



    def add_person(self,user_id):
        """
        Invite a person to this 'date'
        """
        db.session.add(p)
        db.session.commit()

    def describe(self,activity_id):
        """
        Give this date an activity!
        """
        self.activity = activity_id
        db.session.commit()

    def notify(self):
        """
        Tell both people about this time.
        """
        pass

if __name__ == "__main__":

    db.create_all()
    # code to insert goees here.
