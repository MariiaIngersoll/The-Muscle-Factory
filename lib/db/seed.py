from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random 

from models import Member, Trainer, Exercise

fake = Faker()

if __name__ == "__main__":
    engine = create_engine("sqlite:///the_muscle_factory.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Member).delete()
    session.query(Trainer).delete()
    session.query(Exercise).delete()
  