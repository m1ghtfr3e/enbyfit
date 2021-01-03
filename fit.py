
class Body:

    '''
        Body Class.

    :param height: Height of the Person in cm
    :type height:  float
    :param weight: Weight of the Person in kg
    :type weight:  float
    :param hormonal_sex: Hormonal Sex of a person,
                         other "indications" of
                         sex are not needed.
    :type hormonal_sex: string
    '''

    def __init__(self, height, weight, hormonal_sex=''):
        self._height = height
        self._weight = weight
        self._hormonal_sex = hormonal_sex

    @property
    def waist(self):
        return self._waist

    @waist.setter
    def waist(self, waist):
        self._waist = waist

    @property
    def hip(self):
        return self._hip

    @hip.setter
    def hip(self, hip):
        self._hip = hip

    @property
    def bmi(self):
        '''
            Get the BMI.

        The bmi is calculated with
        the weight in kg divided by
        the square ofthe height
        in meters;
        In general the Ponderal Index
        is more expressive.

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

        The ponderal index is calculated
        by the weight in kg divided by
        the height in meters to the
        power of three.

        -> Results between 11 and 14
        are interpreted as normal.

        :return: Returns the Ponderal Index
        :rtype: float
        '''
        return float('%.1f' % (self._weight / ((self._height/100) ** 3)))

    @property
    def broca_index(self):
        '''
            Get Broca Index

        :return: Returns the Broca Index
        :rtype: float
        '''
        return float('%.1f' % (self._weight / (self._height - 100) * 100))

    @property
    def metabolic_rate(self):
        '''
            Get the Basal Metabolic Rate

        The basal metabolic rate is calculated
        with the weight * 24 (hours);
        It is not really expressive, as it is
        igonring body facts which have influence
        on this, like muscle mass.
        It is recommended to use the Harris-
        Benedict Formula instead.

        :return: Returns the Metabolic Rate
        :rtype: integer
        :Example:
            >>> Body(180, 50).metabolic_rate
            1200
        '''
        return int(self._weight * 24)

    @property
    def harris_benedict_formula(self):
        pass

    @property
    def waist2hip_ratio(self):
        '''
            Get the Waist-to-Hip Ratio

        :return: Returns the W-H-Ratio
        :rtype: float
        '''
        try:
            return self._waist / self._hip
        except AttributeError:
            return

    def __repr__(self):
        return f'Body(                          \
            _height={self._height},             \
            _weight={self._weight},             \
            _hormonal_sex={self._hormonal_sex}  \
            )'

    def __str__(self):

        represent = f'''
        Height:             {self._height}
        Weight:             {self._weight}
        Hormonal Sex:       {self._hormonal_sex}

        BMI:                {self.bmi}
                            [Normal: 20-25]

        Ponderal Index:     {self.ponderal_index}
                            [Normal: 11-14]

        Broca Index:        {self.broca_index}
                            [Normal: 90-110]

        Metabolic Rate:     {self.metabolic_rate}

        Waist-to-Hip Ratio: {self.waist2hip_ratio}
        '''
        return represent


class Person:

    '''
        Person class.

    :param name: Name of the Person
    :type name:  string
    :param age:  Age of the Person
    :type age:   integer
    '''

    def __init__(self, name, age):
        self._name = name
        self._age = age


    def __repr__(self):
        return f'Person(_name={self._name}, _age={self._age})'

    def __str__(self):
        represent = f'''
        Name:               {self._name}
        Age:                {self._age}
        '''
        return represent


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    p = Person(name='Borrito', age=21)
    b = Body(165, 48)

    print(p)
    print(b)
