from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random 

from models import Member, Trainer, Exercise


if __name__ == "__main__":
    engine = create_engine("sqlite:///muscle_factory.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Member).delete()
    session.query(Trainer).delete()
    session.query(Exercise).delete()

    fake = Faker()
    
    trainers = []

    list_of_gym_goals = ["Grow Stronger Glutes", "Improve Upper Body Strength", "Build a Stronger Core","Boost Your Cardio Endurance", "Lift Weights", "Increase Your Flexibility","Learn a New Skill"]

    for _ in range(5):
        trainer = Trainer(
            first_name=f"{fake.first_name()}",
            last_name=f"{fake.last_name()}",
            years_of_experience=random.randint(3, 10),
            
        )
        trainers.append(trainer)
        session.add(trainer)
        session.commit()

    
    list_of_gym_goals = ["Grow Stronger Glutes", "Improve Upper Body Strength", "Build a Stronger Core","Boost Your Cardio Endurance", "Lift Weights", "Increase Your Flexibility","Learn a New Skill"]

    

  
    

  