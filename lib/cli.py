import sys
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Member, Trainer, Exercise

engine = create_engine("sqlite:///db/muscle_factory.db")
session = Session(engine, future=True)


def goodbye():
    print("Thank you for checking out our gym! Hope you enjoyed your time here!!!")

def reroute():
    option = 0
    while option != 2:
        print(f"""
            1 - Would you like to go back to the main menu? 
            2 - Exit the program.
            """)
        option = int(input())
        if option == 1:
            main()
        elif option == 2:
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid option. Please select a valid option.")


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
            print("Sure! Pick a class you are the most interested in! We got great options!")
            all = session.query(Exercise).all()
            for i in all:
                print(i)

            reroute()

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
            print("Exiting program")

if __name__ == "__main__":
    main()
   
