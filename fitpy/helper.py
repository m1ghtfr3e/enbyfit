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
    def make_path(self):
        '''
            Creates the Path

        :return: Info that directory was
            created successfully
        :rtype: string
        '''
        os.mkdir(self.root_dir)
        return f'[+] Created directory at: {self.root_dir}'


class FileHandler:
    def __init__(self, name):
        self._file_name = f'{name}_fitpy.json'

    def __enter__(self):
        pass

    def __exit__(self, *exec):
        pass



if __name__ == '__main__':
    p = Person('manon')
    df = MakeFrame(p.__dict__)
    print(df)
