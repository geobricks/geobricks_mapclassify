from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksMapClassify',
    version='0.0.3',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks .',
    install_requires=[
        'watchdog',
        'flask',
        'flask-cors',
	    'numpy',
        'pysal',
        'GeobricksCommon'
    ],
    url='http://pypi.python.org/pypi/GeobricksMapClassify/',
    keywords=['geobricks', 'geoserver', 'sld', 'mapclassify', 'choropleth map']
)
