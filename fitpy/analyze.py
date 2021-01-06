import json
import os
import sys

from person import Person
from body import Body
from sports import Running


class Saver:
    ''' Saver class

    Can write and read
    an overview of
    fitpy.
    '''

    path = f'{os.path.expanduser('~')/fitpy}'

    def __init__(self, save_load, mode):
        self.obj = save_load
        self.mode = mode

        self.__file = f'{self.obj.__id}.csv'

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass
