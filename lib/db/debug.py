from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (Trainer, Member, Exercise)

if __name__ == '__main__':
    engine = create_engine("sqlite:///the_muscle_factory.db")
    session = Session(engine, future=True)

    import ipdb; ipdb.set_trace()