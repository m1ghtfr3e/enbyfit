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
        '''
        self._name = name.capitalize()
        self.__id = None

    def asdict(self):
        return {'name' : self._name}

    def __repr__(self):
        return f'Person(_name={self._name})'

    def __str__(self):
        '''
            Representation of Person
            and passed objects.
        '''

        return f'''\n\t
            Overview of {self._name}
            ==========================
            '''
