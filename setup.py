import os
import sys
import setuptools

HERE = os.abspath(os.path.dirname(__file__))

sys.path.insert(0, HERE)

with open('README.rst', 'r') as f:
    DESCRIPTION = f.read()

REQUIRES = [
    'npyscreen==4.10.5',
    'six==1.15.0',
    'SQLAlchemy==1.3.22',
    'SQLAlchemy-Utils==0.36.8'
]

setuptools.setup(
    name='enbyfit',
    version='0.0.1.dev2',
    author='m1ghtfr3e',
    description='Fitness and Health',
    long_description=DESCRIPTION,
    url='https://github.com/m1ghtfr3e/enbyfit',
    packages=setuptools.find_packages(),
    install_requires=REQUIRES,
    classifiers=[
        'Operating System :: OS Independent',

        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Other Audience',

        'Natural Language :: English',
        'Topic :: Utilities'
        ],
    include_package_data=True,
    python_requires='>=3.7',
    license='GPLv3',
    )
