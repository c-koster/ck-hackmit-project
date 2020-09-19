from my_app import db

class User(db.Model):
    __tablename__ == "users"
    id = db.Column(db.Integer, primary_key=True)

    # contact info
    name = db.Column(db.String(100))
    email = db.Colummn(db.String(100))
    phone = db.Column(db.String(100))

    # personality characteristics
    openness = db.Column(db.Integer())
    consc = db.Column(db.Integer()) # conscientiousness
    extraversion = db.Column(db.Integer())
    agreeable = db.Column(db.Integer())
    neuroticism = db.Column(db.Integer())

    # major?
    major = db.column(String(20)))
    # interests ?


class Activity(db.model):
    __tablename__ == "activities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(800))
    link = db.Column(db.String(100))


class Date(db.model):

    id = db.Column(db.Integer, primary_key=True)
    time = # store its relation to google calendar
