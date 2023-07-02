# import sys
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Member

engine = create_engine("sqlite:///db/muscle_factory.db")
session = Session(engine, future=True)

# sys.path.append('./helper_functions')

# user is able to find trainsers based on their goals. 
def reroute():
    main()

def main():
    print("Hello user! ")
    choice = 0
    while choice !=5:
        print(f'''
          What would like to do today?
          1 - Sign up for a membership
          4 - Exit
           ''')
        choice = int(input())
        if choice == 1:
            print("Lets Sign Up!")
            first_name = input("What is your name?")
            last_name = input("What is your last name?")
            trainings_per_week = int(input("Whats the number of trainings you want to do per week?"))
            gym_goal = input("What is your goal?")

            new = Member(first_name=first_name, 
                        last_name=last_name, 
                        gym_goal=gym_goal,
                        trainings_per_week= trainings_per_week)
            session.add(new)
            session.commit()
            print("WELCOME!")

            reroute()
        if choice == 4:
            print("Goodbye")
            break





if __name__ == "__main__":
    main()