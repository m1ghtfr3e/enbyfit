'''
    Testing the Body Module
'''

import unittest

from enbyfit.body import Body


class TestBody(unittest.TestCase):
    def test_required_attributes(self):
        testbody = Body()
