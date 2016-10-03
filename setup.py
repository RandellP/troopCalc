
from setuptools import setup

setup(name='troopcalc',
    version='0.1',
    description='Calculates troop distribution',
    url='http://github.com/randellpelak/troopcalc',
    author='Randell Pelak',
    author_email='randellpelak@gmail.com',
    packages=['troopcalc', 'troopcalc.tests', 'troopcalc.data'],
    package_dir={'troopcalc': 'troopcalc', 'troopcalc.tests': 'troopcalc/tests', 'troopcalc.data': 'troopcalc/data'},
    package_data={'troopcalc.data': ['*.json']},
    )
