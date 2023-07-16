from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import Session
from db.models import Member, Trainer, Exercise

engine = create_engine("sqlite:///db/muscle_factory.db")
session = Session(engine, future=True)


def reroute():
    option = 0
    while option != 1:
        print(f"""
                    1 - WOULD YOU LIKE TO STAY IN THIS MODULE?
                    2 - GO BACK TO MAIN MENU
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
    while choice !=6:
        print(f'''
                    What would you like to do today?
              
                    1 - I would like to know what kind of exercises and gym classes I can attend as a member of this gym?
              
                    2 - Show me information about your trainers
                    
                    3 - Sign up for a membership
                    
                    4 - Edit my information
                    
                    5 - Cancel my membership
                    
                    6 - Exit
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
                        print("")

                    selected_class = input("Type name of the class to find out more information!!>>>")
                    name_of_class = session.query(Exercise).filter(Exercise.name.ilike(f"%{selected_class}%")).all()
                    if name_of_class:
                        for exercise in name_of_class:
                            print(f"Exercise's Name: {exercise.name}")
                            print(f"Intensity: {exercise.intensity}")
                            print(f"Duration: {exercise.durations}")

                            class_trainer = session.query(Trainer).join(Exercise).filter(Exercise.name.ilike(f"%{selected_class}%")).all()

                            if class_trainer:
                                for trainer in class_trainer:
                                    print("")
                                    print(f"The insctructor for {exercise.name} is {trainer.first_name} {trainer.last_name} with {trainer.years_of_experience} years of experience!")
                            else:
                                print("No trainer found for this exercise.")
                            
                            print("")

                        reroute()
                    else:
                        raise NameError("No matching class found.")
                
                if exercise_choice == 2:
                    filtered_by_intensity = session.query(
                        Exercise.name, Exercise.intensity).order_by(
                        asc(Exercise.intensity)).all()
                    
                    for intense in filtered_by_intensity:
                        exercise_name = intense[0]
                        intensity = intense[1]
                        print("")
                        print(f"Exercise: {exercise_name}")
                        print(f"Intensity: {intensity}")
                        
                    reroute()

                if exercise_choice == 3:
                    filtered_by_duration = session.query(
                        Exercise.name, Exercise.durations).order_by(
                        desc(Exercise.durations)).all()
                    
                    for duration in filtered_by_duration:
                        exercise_name = duration[0]
                        duration = duration[1]
                        print("")
                        print(f"Exercise: {exercise_name}")
                        print(f"Duration: {duration}")
                        
                    reroute()
        
        elif choice == 2:
            all_trainers = session.query(Trainer).all()
            for trainer in all_trainers:
                print(trainer)

            print("")
            trainer_choice = int(input("Type trainer's ID to find out what classes they teach >>> "))
            selected_trainer = session.query(Trainer).filter(Trainer.id == trainer_choice).first().exercises

            # selected_trainer = session.query(Exercise).join(Trainer).filter(Trainer.id == trainer_choice).all()
            for i in selected_trainer:
                print(i)

                                    

        elif choice == 3:
            print("Lets Sign Up!")
            first_name = input("What is your name?")
            last_name = input("What is your last name?")
            trainings_per_week = int(input("Whats the number of trainings you want to do per week?"))
            gym_goal = input("What is your goal?")
            class_choice = input("What class do you wanna take?")

            trainer = session.query(Trainer).join(Exercise).filter(Exercise.name.ilike(f"%{class_choice}%")).first()
            # trainer = session.query(Trainer).filter(Trainer.exercises.any(Exercise.name.ilike(f"%{class_choice}%"))).first()

            new = Member(first_name=first_name, 
                        last_name=last_name, 
                        gym_goal=gym_goal,
                        trainings_per_week= trainings_per_week,
                        trainer_id = trainer.id
                        )
            session.add(new)
            session.commit()
            print("")
            print(f"Welcome to the Muscle Factory gym {new.first_name} {new.last_name}. Hope you enjoy your time here!!! Your instructor is {trainer.first_name} {trainer.last_name} ")
            

        elif choice == 4:
            member_id = input("Please type your member ID in order to access the edit menu>>>")
            members_data = session.get(Member, member_id)
            edit_choice = 0
            while edit_choice != 5:
                print(f"""
                    What information would you like to edit?
                    
                    1 - First name
                    
                    2 - Last Name 
                    
                    3 - Gym Goal
                    
                    4 - Trainings per week
                    
                    5 - Go back to MAIN MENU
                      """
                      )
                edit_choice = int(input())
                if edit_choice == 1:
                    new_name = input("What would you like to change your first name to?>>>")
                    members_data.first_name = new_name
                    session.commit()
                    print(f"Your last name have been changed to {members_data.first_name}")

                if edit_choice == 2:
                    new_name = input("What would you like to change your last name to?>>>")
                    members_data.last_name = new_name
                    session.commit()
                    print(f"Your last name have been changed to {members_data.last_name}")
                
                if edit_choice == 3:
                    new_goal = input("What is new gym goal?!>>>")
                    members_data.gym_goal = new_goal
                    session.commit()
                    print(f"Your new gym goal is {members_data.gym_goal}")

                if edit_choice == 4:
                    trainings_per_week_new = int(input("What is the amount of gym sessions you can attend weekly? Please enter a number.>>>"))
                    members_data.trainings_per_week = trainings_per_week_new
                    session.commit()
                    print(f"Number of gym sessions per week has been updated to {members_data.trainings_per_week}")

        

        elif choice == 5:
            print("We are so sad to see you canceling your membership! :(")
            print("Enter your name and last name in order to proceed with membership cancelation")
            deleted_name = input("Type in your first name>>>")
            deleted_last_name = input("Type in your last name>>>")

            members_data = session.query(Member).filter(Member.first_name.ilike(deleted_name), Member.last_name.ilike(deleted_last_name)).first()
            if members_data is not None:
                session.delete(members_data)
                session.commit()
                print(f"{members_data.first_name} {members_data.last_name} has been deleted!!!")
            else:
                print("No matching member found.")

        else:
            choice = 6
            goodbye()
            
               


def goodbye():
    print("Thank you for checking out our gym! Hope you enjoyed your time here!!!")
    quit()

if __name__ == "__main__":
    main()
   
