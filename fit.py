
class Body:

    '''
        Body Class.

    :param height: Height of the Person in cm
    :type height:  float
    :param weight: Weight of the Person in kg
    :type weight:  float
    '''

    def __init__(self, height, weight):
        self._height = height
        self._weight = weight

    @property
    def bmi(self):
        '''
            Get the BMI.

        :return: Returns the Body-Mass-Index
        :rtype: float

        :Example:
            >>> Body(120, 80).bmi
            55.6
        '''
        return float('%.1f' % (self._weight / ((self._height/100) ** 2)))

    @property
    def ponderal_index(self):
        '''
            Get the Ponderal Index

        :return: Returns the Ponderal Index
        :rtype: float
        :Example:
        '''
        return float('%.1f' % (self._weight / ((self._height/100) ** 3)))

    def __str__(self):

        represent = f'''
        Height:     {self._height}
        Weight:     {self._weight}

        BMI:        {self.bmi}
        Ponderal Index:     {self.ponderal_index}
        '''
        return represent


class Person:

    '''
        Constructor of Person class
        with name and age.

    :param name: Name of the Person
    :param age:  Age of the Person
    :type name:  string
    :type age:   integer
    '''

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        represent = f'''
        Name:   {self._name}
        Age:    {self._age}
        '''
        return represent


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    p = Person(name='manon', age=24)
    b = Body(183, 70)
    print(p)
    print(b)
