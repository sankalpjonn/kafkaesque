# please install python if it is not present in the system
from setuptools import setup

setup(
 name='kafkaesque',
 version='1.0',
 packages=['kafkaesque'],
 install_requires=['kafka-python']
)
