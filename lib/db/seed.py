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


    for _ in range(5):
        trainer = Trainer(
            first_name=f"{fake.first_name()}",
            last_name=f"{fake.last_name()}",
            years_of_experience=random.randint(3, 10),
            
        )
        trainers.append(trainer)
        session.add(trainer)
        session.commit()


    
    list_of_exercises = {
        "1": "Yoga",
        "2": "Pilates",
        "3": "Strength Training",
        "4": "Bicycling",
        "5": "Stretching",
        "6": "Weightlifting",
        "7": "Cycling",
        "8": "High-intensity interval training",
        "9": "Boxing",
    }

    exercises = []

    all = session.query(Trainer).all()

 
    for type in list_of_exercises:
        exercise = Exercise(
            name = list_of_exercises[type],
            intensity = random.randint(4,9),
            durations = str(random.randint(30, 60)) + " Minutes",
            trainer_id=random.choice(all).id
        )
        exercises.append(exercise)
        session.add(exercise)
        session.commit()
    
    list_of_gym_goals = [
        "Grow Stronger Glutes",
        "Improve Upper Body Strength",
        "Build a Stronger Core",
        "Boost Your Cardio Endurance",
        "Lift Weights",
        "Increase Your Flexibility",
        "Learn a New Skill",
    ]

    members = []

    for _ in range(100):
            member = Member(
                first_name=f"{fake.first_name()}",
                last_name=f"{fake.last_name()}",
                gym_goal = random.choice(list_of_gym_goals),
                trainings_per_week = random.randint(2,7),
                trainer_id=random.choice(all).id
            )
            members.append(member)
            session.add(member)
            session.commit()
        

    

  
    

  