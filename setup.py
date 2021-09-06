from os import path
from codecs import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='v6-tidal-py',
    version="1.0.0",
    description='Combines distributed learning with SOLID pods.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MaastrichtU-IDS/v6-tidal-py',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'vantage6-client'
    ]
)