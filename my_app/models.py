from my_app import db

class User(db.Model):
    __tablename__ == "users"
    id = db.Column(db.Integer, primary_key=True)

    # contact info
    name = db.Column(db.String(100))
    email = db.Colummn(db.String(100))
    phone = db.Column(db.String(100))

    # availability ?


    # personality characteristics

    # major?


class User_info(db.Moodeel):

    __tablename__ == "user data"
    id = db.Column(db.Integer, primary_key=True)
