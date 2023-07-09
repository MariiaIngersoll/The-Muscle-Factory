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

## Key Models
Member:

Attributes: id, first name, lasy name, gym goal, trainings per week

Relationships: Belongs to a trainer

Trainer:

Attributes: id, first name, last name, years of experience

Relationships: Has multiple members and exercises 

Exercise:

Attributes: id, name, intensity, duration

Relationships: Belongs to a trainer


## Contributing
If you would like to contribute to this project, feel free to submit pull requests or open issues in the repository.

## Contacts
If you have any questions or suggestions, please contact me at maria.nagornaya1996@gmail.com

Thank you for checking out my program! I hope you enjoy your time at The Muscle Factory Gym!

