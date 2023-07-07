import sys

import importlib
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import Session
from db.models import Member, Trainer, Exercise

engine = create_engine("sqlite:///db/muscle_factory.db")
session = Session(engine, future=True)


def reroute():
    option = 0
    while option != 1:
        print(f"""
            1 - Would you like to stay in this module? 
            2 - I wanna go back to main menu
            """)
        option = int(input())
        if option == 1:
            print("")

        if option == 2:
            print("")
            main()
            

def main():
    print(f"""
                            Hello user!
                    Welcome to The Muscle Factory Gym!""")
    choice = 0
    while choice !=5:
        print(f'''
                    What would like to do today?
                    1 - I would like to know what kind of exercises and gym classes I can attend as a member of this gym?
                    
                    2 - Sign up for a membership
                    
                    3 - Edit my information
                    
                    4 - Cancel my membership
                    
                    5 - Exit
                    ''')
        choice = int(input())
        if choice == 1:
            exercise_choice = 0
            
            while exercise_choice != 4:

                print("""
                    1 - Browse all the classes we have!
                    2 - Filter classes by intensity
                    3 - Filter classes by duration
                    4 - Go back to main menu
                        """
                        )
                exercise_choice = int(input())
                all = session.query(Exercise).all()
                if exercise_choice == 1:
                    
                    for i in all:
                        print(i.name)

                    selected_class = input("Type name of the class to find out more information!!>>>")
                    name_of_class = session.query(Exercise).filter(Exercise.name.ilike(f"%{selected_class}%")).all()
                    for class_ in name_of_class:
                        print(class_)
                    
                    reroute()
                from sqlalchemy import desc

                if exercise_choice == 2:
                    filtered_by_intensity = session.query(Exercise.name, Exercise.intensity).order_by(asc(Exercise.intensity), Exercise.name).all()
                    for intense in filtered_by_intensity:
                        exercise_name = intense[0]
                        intensity = intense[1]
                        print(f"Exercise: {exercise_name}")
                        print(f"Intensity: {intensity}")
                                    


                

        elif choice == 2:
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
            print("Welcome to the Muscle Factory gym. Hope you enjoy your time here!!!")
            reroute()

        elif choice == 3:
            
           print("BUTTTTT")
           reroute()

        elif choice == 4:
            print("HUHHHHH")
            reroute()

        elif choice == 5:
            goodbye()
            sys.exit(0)

def goodbye():
    print("Thank you for checking out our gym! Hope you enjoyed your time here!!!")

if __name__ == "__main__":
    main()
   
