# Phase 3 CLI Project "The Muscle Factory Gym"

# Introduction
Welcome to The Muscle Factory Gym! This CLI program is a command-line application designed to manage various operations related to a gym, including exercise browsing, trainer information, membership sign-up, editing member information, and membership cancellation.

## Installation
Before running the program, make sure you have the following dependencies installed:

Python (version 3.x)
SQLAlchemy
You can install SQLAlchemy using the following command:
pip install SQLAchemy

Clone this repository to your local machine and navigate to its directory.
Run pipenv install to install all the necessary package dependencies.
Run pipenv shell to enter the virtual environment.
Navigate to the lib/db directory and run python seed.py to populate the database with mock data.
Return to the lib directory by running cd ..
Run "python cli.py" to start using The Muscle Factory Gym program.

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


## Contributing
If you would like to contribute to this project, feel free to submit pull requests or open issues in the repository.

## Contacts
If you have any questions or suggestions, please contact me at maria.nagornaya1996@gmail.com

Thank you for checking out my program! I hope you enjoy your time at The Muscle Factory Gym!

