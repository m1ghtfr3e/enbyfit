'''
    Models for the Enbyfit Database

There are three different Base Models which
represent eacht Table in our Databse.
'''


from sqlalchemy import Column, Integer, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserDB(Base):
    '''
        Model of User Database
    '''
    __tablename__ = 'UserDB'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    dataset = Column(JSON, nullable=False)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}, {self.__tablename__}'


class BodyDB(Base):
    '''
        Model of Body Database
    '''
    __tablename__ = 'BodyDB'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    data = Column(JSON, nullable=False)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}, {self.__tablename__}'


class ActivityDB(Base):
    '''
        Model of Acitvity Database
    '''
    __tablename__ = 'AcitivtyDB'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    data = Column(JSON, nullable=False)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}, {self.__tablename__}'
