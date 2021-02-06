'''
    Helper Module for fitpy

:class: FitUser - db Model
:class: Database - db operations
'''

import datetime
import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker

from enbyfit import Person
from enbyfit import Body
from enbyfit import Running


Base = declarative_base()


class FitUser(Base):
    '''
        Model of User
    Model class of the User
    '''
    __tablename__ = 'fitpyuser'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    dataset = Column(JSON, nullable=False)

# Edit Database !
class Database:
    '''
        Database of enbyfit
    Enables us to communicate
    with our User Database.
    '''
    engine = db.create_engine('sqlite:///enbyfit.db')
    session = sessionmaker(bind=engine)
    Session = session()

    def __init__(self) -> None:
        if not database_exists(self.engine.url):
            self.make_database()

    def make_database(self) -> None:
        '''
        Create a database if none exists.
        '''
        Base.metadata.create_all(self.engine)

    def make_entry(self, data: dict) -> None:
        '''
        Make a (new) Entry in Database.
        '''
        new_entry = FitUser()
        #new_entry.id = data[id]
        new_entry.date = datetime.datetime.now()
        new_entry.dataset = data

        self.Session.add(new_entry)
        self.Session.commit()

    def make_query(self, name: str) -> tuple:
        '''
        Make a query from Database.
        '''
        data = []
        for item in self.Session.query(FitUser).all():
            print(item.dataset)
            if name in item.dataset.items():
                data.append(item)
        return data



if __name__ == '__main__':
    d = Database()

    ex1 = {'1': 'a'}
    ex2 = {'name': 'manon'}

    d.make_entry(ex1)
    d.make_entry(ex2)

    print(d.make_query('manon'))
