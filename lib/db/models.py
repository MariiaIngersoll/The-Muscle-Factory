from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trainer(Base):
    __tablename__ = 'trainers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    years_of_experience = Column(Integer())

    def __repr__(self):
        f"Id: {self.id}, " \
        + f"Name: {self.first_name} {self.last_name}, " \
        + f"Years of experience: {self.years_of_experience}"
        