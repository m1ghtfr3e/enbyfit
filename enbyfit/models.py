from sqlalchemy import Column, Integer, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class FitUser(Base):
    '''
        Model of User
    Model class of the User
    '''
    __tablename__ = 'UserDB'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    dataset = Column(JSON, nullable=False)

    def __repr__(self):
        return f'FitUser(id={self.id}, date={self.date}, data={self.dataset})'


class BodyProperties(Base):
    __tablename__ = 'BodyPropertyDB'

    ...


class Activities(Base):
    __tablename__ = 'AcitivtyDB'

    ...
