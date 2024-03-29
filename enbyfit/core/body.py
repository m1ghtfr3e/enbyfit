'''
    Body module.

Defines a Body object for the
Person's object in fitpy.
Person and Body are defined
independently, but can be
defined together.
Both objects can also be added
and/or use the objects defined
in sports.py .
'''

# from . import exceptions


class Body:

    '''
        Body Class.

    :param age: Age of the Person in years
    :type age: int, protected
    :param height: Height of the Person in cm
    :type height:  float, protected
    :param weight: Weight of the Person in kg
    :type weight:  float, protected
    :param hormonal_sex: Hormonal Sex of the Person
    :type hormonal_sex: string, protected
    :param waist: Waist size of the Person in cm
    :type waist: float, protected
    :param hip: Hip size of the Person in cm
    :type hip: float, protected
    '''

    def __init__(self,
        age: int,
        height: float,
        weight: float,
        hormonal_sex: str = None,
        waist: float = None,
        hip: float = None,
        ) -> None:

        super().__init__()

        self._age = age
        self._height = height
        self._weight = weight
        self._hormonal_sex = hormonal_sex
        self._waist = waist
        self._hip = hip

    @property
    def bmi(self) -> float:
        '''
            Get the BMI.

        The bmi is calculated with the weight in kg
        divided by the square ofthe height in meters;
        In general the Ponderal Index is more
        expressive.
        The higher the BMI, the higher are risks for
        certain diseases like cardiovascula disease,
        high blood pressure, type 2 diabetes, gallstones,
        breating problems, and certain types of cancers.
        It may overestimate body fat for athletes and
        people who have a muscular build and
        underestimate body fat for older people and
        those who have lost muscle mass.

        :return: Returns the Body-Mass-Index
        :rtype: float

        :Example:
            >>> Body(22, 120, 80).bmi
            55.6
        '''
        return float('%.1f' % (self._weight / ((self._height/100) ** 2)))

    @property
    def ponderal_index(self) -> float:
        '''
            Get the Ponderal Index

        The ponderal index is calculated by the weight
        in kg divided by the height in meters to the
        power of three.

        -> Results between 11 and 14
           are interpreted as normal.

        :return: Returns the Ponderal Index
        :rtype: float
        '''
        return float('%.1f' % (self._weight / ((self._height/100) ** 3)))

    @property
    def broca_index(self) -> float:
        '''
            Get Broca Index

        :return: Returns the Broca Index
        :rtype: float
        '''
        return float('%.1f' % (self._weight / (self._height - 100) * 100))

    @property
    def metabolic_rate(self) -> int:
        '''
            Get the Basal Metabolic Rate

        The basal metabolic rate is calculated with
        the weight * 24 (hours).
        It is not really expressive, as it is igonring
        body facts which have influence on this,
        like muscle mass.
        It is recommended to use the Harris-Benedict-
        Formula instead.

        :return: Returns the Metabolic Rate
        :rtype: int
        :Example:
            >>> Body(22, 180, 50).metabolic_rate
            1200
        '''
        return int(self._weight * 24)

    @property
    def harris_benedict_equation(self) -> int:
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

            else:
                return 'Raise Error'

        except AttributeError as no_hormsex:
            pass
        else:
            pass

    @property
    def waist2hip_ratio(self) -> float:
        '''
            Get the Waist-to-Hip Ratio

        The Waist-to-Hip Ratio can be a marker for
        cardiovascular diseases. The risk for
        those diseases is more signalised by  the
        allocation of fat around the body than by
        "overweight".

        :return: Returns the W-H-Ratio
        :rtype: float
        '''
        try:
            return self._waist / self._hip

        except AttributeError:
            pass
        except TypeError:
            pass
        else:
            pass

    @property
    def waist2height_ratio(self) -> float:
        ''' Get the Waist-to-Height Ratio
        ...

        :return: Returns Waist-to-Height-Ratio
        :rtype: float
        '''
        try:
            return self._waist / self._height

        except AttributeError:
            pass
        except TypeError:
            pass
        else:
            pass

    @property
    def training_heartrate(self) -> int:
        '''
            Heart Rate for Training

        The following << Max Heartrate >> is
        more for people doing frequently sports,
        whereas this equation should be used
        if you start doing sports or had
        diseases before.

        :returns: Heart Rate for Training
            (in BPM)
        :rtype: int
        '''
        return 180 - self._age

# Add informations!
    @property
    def max_heartrate(self) -> int:
        '''
         Age predicted Maximum Heart Rate

        Different equations are existing
        and there is no way of determining
        which equation suits better or is
        more precisely for each individual.

        Three different equations can be
        used here:
            - The most common equation 
              (which is getting quite
               unprecisely for persons
               aged over 40)

            - A more precise formula for 
              age 40+ people 

            - A generally more precise
              formula 

        (BPM)

        :returns: The max Heart Rate
        :rtype: int
        '''
        # EDIT !
        if ... == 'common':
            return 220 - self._age
        elif self._age >= 40:
            return 207 - (0.7 * self._age)
        elif ... == 'general':
            return 211 - (0.64 * self._age)

    @property
    def target_heartrate_zone(self) -> float:
        '''
        Getting optimal zone of heartrate

        :return: Heartrate Zone
        :rtype: float
        '''
        return float('%2.f' % (self.max_heartrate * 0.85))

    def asdict(self) -> dict:
        '''
            As dict Module

        Get all param as dict.

        :return: Dicitonary of all attributes
            of :class:
        :rtype: dict
        '''
        try:
            param_dict = {
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

        except AttributeError:
            pass
        else:
            pass

        return param_dict

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}, {self.__dict__}'

    def __str__(self) -> str:

        represent = f'''\n
        Age:                {self._age}

        Height:             {self._height}
        Weight:             {self._weight}
        Hormonal Sex:       {self._hormonal_sex}

        BMI:                {self.bmi}

        Ponderal Index:     {self.ponderal_index} kg/m³

        Broca Index:        {self.broca_index}

        Metabolic Rate:     {self.metabolic_rate} kcal

        Harris-Benedict:    {self.harris_benedict_equation} kcal

        Waist-to-Hip Ratio: {self.waist2hip_ratio}

        Waist-to-Height-Ratio: {self.waist2height_ratio}
        '''
        return represent


if __name__ == '__main__':
    import doctest
    doctest.testmod()
