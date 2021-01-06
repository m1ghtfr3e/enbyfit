'''
    Person module

Defines a Person object.
'''

from uuid import uuid4

class Person:

    '''
        Person class.

    The Person class is representing
    an User and related objects like
    Body, Sport, etc.

    :param name: Name of the Person
    :type name:  string
    :param obj_names: Name of the object given
    :type obj_names: string
    :param obj: Objects passed
    :type obj: class
    '''

    def __init__(self, name):
        '''
            Constructor of Persons class

        Accepting **kwargs as optional parameter,
        classes are passed to represent on overview
        of the Person and its related objects.

        :param name: Name of the Person
        :type name: string, protected
        :param id: Id of the Person,
            each person will recieve
            a unique id number
        :type id: str
        '''
        self._name = name.capitalize()
        self._id = None

    def create_id(self):
        self._id = str(uuid4())

    def asdict(self):
        '''
            As dict Module

        Get all param as dict.

        :return: Dicitonary of all attributes
            of :class:
        :rtype: dict
        '''
        return {'name' : self._name}

    def __repr__(self):
        return f'Person(_name={self._name})'

    def __str__(self):
        return f'''\n\t
            Overview of {self._name}
            ==========================
            '''

if __name__ == '__main__':
    p = Person('bolo')
    print(p.create_id())
