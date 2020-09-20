"""
Put in some fake data to work with !!
"""
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

import random
base = os.path.abspath(os.path.dirname(__file__))

engine = create_engine("sqlite:///" + os.path.join(base, 'app.db'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    u1 = User(name="Culton Koster", email="ckoster@middlebury.edu",phone="2128675309",openness=2,consc=3,extraversion=4,agreeable=5,neuroticism=1,major="Computer Science")
    add(u1)
    u2 = User(name="Brandon Brandon", email="blei37168@gmail.com",phone="2128675309",openness=2,consc=3,extraversion=4,agreeable=5,neuroticism=1,major="Mathematics")
    add(u2)

    time1 = Date(time_descriptor="10am",name="chess game",description="Play a chess game together!",link="https://chess.com/")
    time2 = Date(time_descriptor="11am",name="nyt article",description="Read this article from NYT arts and talk about it!",link="https://www.nytimes.com/2020/09/18/theater/static-apnea-review.html")
    time3 = Date(time_descriptor="12pm",name="philosophical question",description="Is hummus a soup?",link="https://plato.stanford.edu/")
    add(time1)
    add(time2)
    add(time3)


def add(row):
    db.add(row)
    db.commit()


if __name__ == "__main__":

    main()
