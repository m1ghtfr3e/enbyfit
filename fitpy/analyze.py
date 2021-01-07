import json
import os
import sys
from pathlib import Path

from person import Person
from body import Body
from sports import Running


class Saver:
    ''' Saver class

    Can write and read
    an overview of
    fitpy.
    '''

    root_dir = f'{Path.home()}/.fitpy'

    def __init__(self,):
        pass

    @classmethod
    def change_rootdir(cls, path):
        '''
            Change Root Directory

        If user wants to specify own
        path.
        '''
        cls.root_dir = path


    def check_path(self):
        '''
            Checks if path is
            existing.
        '''
        if os.path.exists(self.root_dir):
            return True
        else:
            os.mkdir(self.root_dir)
            return '[+] Created directory'


if __name__ == '__main__':
    p = Person('manon')
    s = Saver()
    s.check_path()
