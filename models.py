import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



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


class Activity(db.Model):
    __tablename__ = "activities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(800))
    link = db.Column(db.String(100))


class Date(db.Model):
    __tablename__ = "scheduled_dates"
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.Integer, db.ForeignKey("activities.id"), nullable=True)

    #time =# store its relation to google calendar


    def add_person(self,user_id):
        """
        Invite a person to this 'date'
        """

        pass

    def describe(self,activity_id):
        """
        Give this date an activity!
        """

        pass

    def notify(self):
        """
        Tell both people about this time.
        """
        pass

if __name__ == "__main__":
    db.create_all()
    # code to insert goees here.
