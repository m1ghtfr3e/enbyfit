'''
    Person module

Defines an User object.

Base of any Dataset.
A Person has just two
Parameters:
    - Name
    - A Generated ID

Methods:
    - Asdict
'''

class User:

    '''
        User class.

    The User class is representing
    a Person* and related objects like
    Body, Sport, etc.

    :param name: Name of the User
    :type name:  string
    :param obj_names: Name of the object given
    :type obj_names: string
    :param obj: Objects passed
    :type obj: class
    '''

    def __init__(self, name: str) -> None:
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
        self.__id = str(hash(self._name))[3:8]


    def asdict(self) -> dict:
        '''
            As dict Module

        Get all param as dict.

        :return: Dicitonary of all attributes
            of :class:
        :rtype: dict
        '''
        return {'name' : self._name, 'id' : self.__id}

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}, {self.__dict__}'

    def __str__(self) -> str:
        return f'''\n\t
            Overview of {self._name}
            ==========================
            '''

if __name__ == '__main__':
    pass
