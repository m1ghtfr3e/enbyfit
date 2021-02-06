'''
    Helper Module for fitpy

:class: FitUser - db Model
:class: Database - db operations
'''

import datetime
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker

from enbyfit import Person
from enbyfit import Body
from enbyfit import Running

from models import Base, FitUser, BodyProperties, AcitivtyDB



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
        for item in self.Session.query(FitUser).filter_by(name).all():
            print(item.dataset)
            if name in item.dataset.items():
                data.append(item)
        return data



if __name__ == '__main__':
    ...
