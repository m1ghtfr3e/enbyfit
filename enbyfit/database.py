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


from .user import User
from .body import Body
from .activity import Running

from .models import Base, UserDB, BodyDB, ActivityDB


ENGINE = db.create_engine('sqlite:///enbyfit.db')
SESSION = sessionmaker(bind=ENGINE)


# Edit Database !
class Database:
    '''
        Database of enbyfit
    Enables us to communicate
    with our User Database.
    '''
    Session = SESSION()

    def __init__(self) -> None:
        if not database_exists(ENGINE.url):
            self.make_database()

    def make_database(self) -> None:
        '''
        Create a database if none exists.
        '''
        Base.metadata.create_all(ENGINE)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} -> {self.engine}'


    """
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
    """


if __name__ == '__main__':
    ...
