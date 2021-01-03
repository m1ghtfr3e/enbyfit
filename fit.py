import exceptions


class Body:

    '''
        Body Class.

    :param age: Age of the Person in years
    :type age: int
    :param height: Height of the Person in cm
    :type height:  float
    :param weight: Weight of the Person in kg
    :type weight:  float
    '''

    def __init__(self, age, height, weight):
        self._age = age
        self._height = height
        self._weight = weight

    @property
    def hormonal_sex(self):
        ''' Get Hormonal Sex. '''
        return self._hormonal_sex

    @hormonal_sex.setter
    def hormonal_sex(self, sex):
        ''' Set Hormonal Sex. '''
        self._hormonal_sex = sex

    @property
    def waist(self):
        ''' Get Waist size. '''
        return self._waist

    @waist.setter
    def waist(self, waist):
        ''' Set Waist size. '''
        self._waist = waist

    @property
    def hip(self):
        ''' Get Hips size. '''
        return self._hip

    @hip.setter
    def hip(self, hip):
        ''' Set Hips size. '''
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
            >>> Body(22, 120, 80).bmi
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
        :rtype: int
        :Example:
            >>> Body(22, 180, 50).metabolic_rate
            1200
        '''
        return int(self._weight * 24)

    @property
    def harris_benedict_equation(self):
        '''
            Get the BMR based on the
            Harris-Benedict equation

        Hormonal Female:
            BMR = 655 + (9.6 X weight in kilos)
                + (1.8 X height in cm) – (4.7 x age in years)

        Hormonal Male:
            BMR = 66 + (13.7 x weight in kilos)
                + (5 x height in cm) – (6.8 x age in years)

        :return: Returns the Daily calory need
        :rtype: int

        if obj._hormonal_sex is not defined:
            :raises AttributeError
        '''

        try:
            if self._hormonal_sex == 'male':
                return int(66 + (13.7 * self._weight) \
                        + (5 * self._height) \
                        - (6.8 * self._age))

            elif self._hormonal_sex == 'female':
                return int(655 + (9.6 * self._weight) \
                        + (1.8 * self._height) \
                        - (4.7 * self._age))

        except AttributeError:
            raise exceptions.HormonalSexNotDefined

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
            raise exceptions.WaistOrHipNotDefined

    def __repr__(self):
        represent = f'''Body(
            _height={self._height},
            _weight={self._weight},
            )'''
        return represent

    def __str__(self):

        represent = f'''
        Age:                {self._age}
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

        Harris-Benedict:    {self.harris_benedict_equation}

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
    b = Body(21, 165, 48)

    #b._hormonal_sex = 'female'
    b.harris_benedict_equation
    print(b)
