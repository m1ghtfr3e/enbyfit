import exceptions
from sports import Running

class Body:

    '''
        Body Class.

    :param age: Age of the Person in years
    :type age: int, private
    :param height: Height of the Person in cm
    :type height:  float, private
    :param weight: Weight of the Person in kg
    :type weight:  float, private
    :param hormonal_sex: Hormonal Sex of the Person
    :type hormonal_sex: string, private
    :param waist: Waist size of the Person in cm
    :type waist: float, private
    :param hip: Hip size of the Person in cm
    :type hip: float, private
    '''

    def __init__(self, age, height, weight,
                    hormonal_sex=None,
                    waist=None,
                    hip=None,
                ):
        super().__init__()

        self._age = age
        self._height = height
        self._weight = weight
        self._hormonal_sex = hormonal_sex
        self._waist = waist
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
            :raise: AttributeError
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
        except:
            pass

    def asdict(self):
        return {
            'age' : self._age,
            'height' : self._height,
            'weight' : self._weight,
            'hormonal_sex' : self._hormonal_sex,
            'waist' : self._waist,
            'hip' : self._hip,
            'bmi' : self.bmi,
            'ponderal' : self.ponderal_index,
            'broca' : self.broca_index,
            'metabolic' : self.metabolic_rate,
            'hbe' : self.harris_benedict_equation,
            'w2h' : self.waist2hip_ratio,
        }

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
        :type name: string, private
        :param id: Id of the Person,
            each person will recieve
            a unique id number
        '''
        self._name = name
        self.__id = None

    def asdict(self):
        return {'name' : self._name}

    def __repr__(self):
        return f'Person(_name={self._name}, __obj_names={self.__obj_names})'

    def __str__(self):
        '''
            Representation of Person
            and passed objects.
        '''

        return f'\tOverview of {self._name}'



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    b = Body(21, 165, 48)
    s = Running(b, 11, 60)
    p = Person('borrito')

    overview = p.__str__() + b.__str__() + s.__str__()
    print(overview)
