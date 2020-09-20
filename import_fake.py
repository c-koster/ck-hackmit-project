"""
Put in some fake data to work with !!
"""
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


base = os.path.abspath(os.path.dirname(__file__))

engine = create_engine("sqlite:///" + os.path.join(base, 'app.db'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    

if __name__ == "__main__":
    main()
    #db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY,username VARCHAR NOT NULL, password VARCHAR NOT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)");
    #db.execute("CREATE TABLE reviews (id SERIAL PRIMARY KEY, userid INTEGER REFERENCES users, isbn VARCHAR REFERENCES books, text VARCHAR NOT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)");
    #db.commit()
