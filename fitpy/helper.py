'''
    Helper Modules for fitpy

:class: PrepareFile: Writing and loading data from file
'''

import os, sys
import pandas as pd
from pathlib import Path

from . import Person
from . import Body
from . import Running



class MakeFrame(pd.Series):
    @property
    def _constructor(self):
        return MakeFrame


class PrepareFile:
    '''
        PrepareFile class

    Can write and read
    an overview of
    fitpy.
    '''

    root_dir = f'{Path.home()}/.fitpy/'

    @classmethod
    def change_rootdir(cls, path):
        '''
            Change Root Directory

        If user wants to specify own
        path.

        :return: Info that directory has changed
            to desired path
        :rtype: string
        '''
        cls.root_dir = path

        return f'[+] Root directory changed to {path}'

    @classmethod
    def change_filename(cls, name):
        '''
            Change File Name

        If user wants to specify own
        file.

        :rtype: string
        '''
        cls.file_name = name

        return f'[+] Filename changed to {name}'

    @classmethod
    def make_path(cls):
        '''
            Creates the Path

        :return: Info that directory was
            created successfully
        :rtype: string
        '''
        os.mkdir(cls.root_dir)
        return f'[+] Created directory at: {cls.root_dir}'


class FileHandler:
    def __init__(self, name, mode, to_write=None):
        self._file_name = f'{name}_fitpy.json'
        self.to_write = to_write

        self.__file = open(self._file_name, self._mode)

        if mode == 'w':
            self.write_mode()
        elif mode == 'a':
            self.append_mode()
        elif mode == 'r':
            self.read_mode()

    def write_mode(self):
        self.__file.write(self.to_write)

    def append_mode(self):
        self.__file.write(self.to_write)

    def read_mode(self):
        self.__file.read()



if __name__ == '__main__':
    p = Person('manon')

    with FileHandler('manon', 'w', 'cou cou')as f:
        f.write()
