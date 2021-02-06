import unittest
from enbyfit import Body

# Order of params
# Age, Height, Weight, Hormonak Sex, Waist, Hip
test_body1 = Body(20, 170, 70, 'male')
test_body2 = Body(30, 180, 80, 'female')


class BasicBodyTests(unittest.TestCase):
    def test_bmi(self):
        ...
