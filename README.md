# Phase 3 CLI Project "The Muscle Factory Gym"

# Introduction
Welcome to The Muscle Factory Gym! This CLI program is a command-line application designed to manage various operations related to a gym, including exercise browsing, trainer information, membership sign-up, editing member information, and membership cancellation.

## Installation
Before running the program, make sure you have the following dependencies installed:

Python (version 3.x)
SQLAlchemy
You can install SQLAlchemy using the following command:
pip install SQLAchemy

``` Clone this repository to your local machine and navigate to its directory.
Run pipenv install to install all the necessary package dependencies.
Run pipenv shell to enter the virtual environment.
Navigate to the lib/db directory and run python seed.py to populate the database with mock data.
Return to the lib directory by running cd ..
Run "python cli.py" to start using The Muscle Factory Gym program. ```

## Database
The program uses an SQLite database to store member, trainer, and exercise data. The database file is located at db/muscle_factory.db. The database schema is defined in db/models.py. You can modify the schema by editing this file.

## Models
The models.py file contains the SQLAlchemy models for the entities used in the Muscle Factory Gym program. Here's an overview of the models:

Trainer: Represents a gym trainer. It has the following attributes:

id: Unique identifier for the trainer.
first_name: First name of the trainer.
last_name: Last name of the trainer.
years_of_experience: Number of years of experience of the trainer.
members: Relationship to the Member model, representing the members trained by the trainer.
exercises: Relationship to the Exercise model, representing the exercises taught by the trainer.

Member: Represents a gym member. It has the following attributes:

id: Unique identifier for the member.
first_name: First name of the member.
last_name: Last name of the member.
gym_goal: Goal of the member in the gym.
trainings_per_week: Number of gym trainings the member wants to do per week.
trainer_id: Foreign key referencing the id of the trainer 

Exercise: Represents a gym exercise or class. It has the following attributes:

id: Unique identifier for the exercise.
name: Name of the exercise.
intensity: Intensity level of the exercise.
durations: Duration of the exercise.
trainer_id: Foreign key referencing the id of the trainer who teaches the exercise.
Each model also provides a __repr__() method to display meaningful representations of the objects.

Seeding the Database
To populate the database with initial data, you can use the seed.py script. This script inserts sample member, trainer, and exercise records into the database. Cd into lib/db and then run the script using the following command:

python seed.py

## Command-Line Interface (CLI)
The cli.py file contains the command-line interface for the Muscle Factory Gym program. It provides a convenient way to interact with the program using commands instead of the menu. Cd into lib directory and run the CLI using the following command:

python cli.py

The program will display a menu with various options. Use the corresponding numbers to select an action.

Option 1: Browse exercise classes
Option 2: View trainer information
Option 3: Sign up for a membership
Option 4: Edit member information
Option 5: Cancel membership
Option 6: Exit the program
Follow the prompts and enter the required information to perform each action.


When you select option 1 from the main menu in your program, the following sequence of actions will occur:

The program will display a sub-menu related to exercise browsing.

It will prompt you to select an option:

Option 1: Browse all the classes available.
Option 2: Filter classes by intensity.
Option 3: Filter classes by duration.
Option 4: Go back to the main menu.
You will need to enter the corresponding number for your desired option.

Based on your selection, the program will perform the following actions:

Option 1: Browse all classes:

The program will retrieve all exercise classes from the database.
It will then display the names of all the classes.
You will be prompted to enter the name of a specific class to get more information.
The program will find the class based on the name you provided and display detailed information about the exercise, including its name, intensity, duration, and the instructor's name and years of experience.
If no matching class is found, a NameError will be raised.
After displaying the information, you will be redirected to the reroute() function.

Option 2: Filter classes by intensity:

The program will query the database and retrieve exercise classes, ordered by intensity in ascending order.
It will display the exercise name and intensity for each class.
After displaying the information, you will be redirected to the reroute() function.

Option 3: Filter classes by duration:

The program will query the database and retrieve exercise classes, ordered by duration in descending order.
It will display the exercise name and duration for each class.
After displaying the information, you will be redirected to the reroute() function.

Option 4: Go back to the main menu.
You will be redirected back to the main menu.

If you select option 2 from main menu "View Trainer Information":

Retrieves information about all the gym trainers from the database.
Displays the trainer information, including their IDs, names, and years of experience.
Prompts you to enter the ID of a trainer to see the classes they teach.
Retrieves the exercise classes taught by the selected trainer and displays their names.

If you select option 3 from main menu " Sign up for a Membership":
Prompts you to enter your name, last name, number of trainings per week, gym goal, and the class you want to take.
Finds a trainer for the chosen class and assigns them as your instructor.
Creates a new member record in the database with the provided information.
Displays a welcome message with your name and the name of your instructor.


If you select option 4 from main menu "Edit Member Information":
Prompts you to enter your member ID.
Displays a sub-menu to choose the information you want to edit: first name, last name, gym goal, trainings per week, or go back to the main menu.
Performs the corresponding edit based on your selection.
Updates the member information in the database.
Displays a confirmation message with the updated information.

If you select option 5 from main menu "Cancel Membership":

Prompts you to enter your member ID to confirm the cancellation.
Retrieves your member record from the database.
Deletes your member record.
Displays a confirmation message with your name and a farewell message.

Option 6: Exit the Program

Displays a farewell message.
Exits the program.


## Contributing
If you would like to contribute to this project, feel free to submit pull requests or open issues in the repository.

## License
Licensing is not being offered at this time. For any questions, please reach out to our support team.

## Contacts
If you have any questions or suggestions, please contact me at maria.nagornaya1996@gmail.com

Thank you for checking out my program!
